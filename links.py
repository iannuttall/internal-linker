import os
import sys
import re
import spacy
from spacy.matcher import Matcher, PhraseMatcher
from collections import defaultdict
from keywords import KeywordExtractor
from numpy import dot
from numpy.linalg import norm
from dotenv import load_dotenv
load_dotenv()

class InternalLinker:
    def __init__(self, input_directory, output_directory, prefix="/blog"):
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.prefix = prefix
        self.nlp = spacy.load("en_core_web_md")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr='LOWER')
        self.keyword_extractor = KeywordExtractor(self.input_directory)
        self.keywords_data = self.keyword_extractor.extract_keywords_for_directory()

    def find_places_for_links(self, text, keywords_data, filepath):
        text = self._clean_text(text)  # Clean text first
        doc = self.nlp(text)
        potential_links = {}
        used_urls = set()
        
        for file, keywords in keywords_data.items():
            if file == os.path.basename(filepath):  # check if the file is the current file
                continue

            result, modified_content, used_urls, fallback_info, suggestion_data = self._build_anchor_text(doc, keywords, file, used_urls)
            if result:
                anchor_text = suggestion_data["anchor_text"]
                if anchor_text not in potential_links or suggestion_data["score"] > potential_links[anchor_text]["data"]["score"]:
                    potential_links[anchor_text] = {
                        "link_filename": file,
                        "data": suggestion_data
                    }

        potential_links = self._refine_potential_links(potential_links)

        word_count = len(text.split())
        max_links = (word_count // 1000) * 10
        # return dict(list(potential_links.items()))
        return dict(list(potential_links.items())[:max_links])
    
    def _refine_potential_links(self, potential_links):
        refined_links = {}
        for anchor_text, link_data in potential_links.items():
            keyword = link_data["data"]["keyword"]
            if self.is_semantically_similar(anchor_text, keyword):
                refined_links[anchor_text] = link_data
        return refined_links
    
    def _generate_keyword_variations(self, keywords):
        """
        Generate variations of the provided keywords by including both the original and lemmatized forms. All returned keywords are in lowercase and duplicates are removed.
        """
        keyword_variations_set = set()
        for keyword in keywords:
            lower_keyword = keyword.lower()
            lemmatized_keyword = ' '.join([token.lemma_ for token in self.nlp(lower_keyword)])
            
            keyword_variations_set.add(lower_keyword)
            keyword_variations_set.add(lemmatized_keyword)
            
        return list(keyword_variations_set)

    def _initialize_matcher(self, keyword_variations):
        """
        Initialize the PhraseMatcher with the provided keywords.
        """
        matcher = Matcher(self.nlp.vocab)
        for keyword_variation in keyword_variations:
            keyword_pattern = self._create_keyword_pattern(keyword_variation)
            matcher.add(f'KEYWORD_{keyword_variation}', [keyword_pattern])
        return matcher
    
    def _create_keyword_pattern(self, keyword_variation):
        """
        Create a pattern for the provided keyword variation.
        """
        keyword_tokens = self.nlp(keyword_variation)
        pattern = []
        
        # Start of string or preceded by a space (improves boundary detection)
        pattern.append({'ORTH': '^', 'OP': '?'})
        pattern.append({'IS_SPACE': True, 'OP': '?'})
        
        for token in keyword_tokens:
            if not token.is_stop:
                # Using lemma for flexibility in matching
                pattern.append({'LEMMA': {'REGEX': f'(?i){re.escape(token.lemma_)}'}})
                pattern.append({'IS_SPACE': True, 'OP': '?'})
        
        # End of string or followed by a space (improves boundary detection)
        pattern.append({'ORTH': '$', 'OP': '?'})
        
        return pattern
    
    def _build_anchor_text(self, text, keywords, url, used_urls=None):
        if used_urls is None:
            used_urls = set()

        # Check used URLs at the start
        if url in used_urls:
            return "", text, used_urls, {}, {}
        
        keyword_variations = self._generate_keyword_variations(keywords)
        matcher = self._initialize_matcher(keyword_variations)
        matches_found = matcher(text)

        if not matches_found:
            return "", text, used_urls, {}, {}
        
        matches, used_anchors, potential_links, location_of_link, suggestion_data = self._process_matches(text, matches_found, keyword_variations, url, used_urls)

        if matches:
            output_strings = self._generate_output_strings(matches)
            return "\n".join(output_strings), location_of_link, used_urls, {}, suggestion_data
        
        return "", text, used_urls, {}, {}
    
    def _generate_output_strings(self, matches):
        output_strings = []
        for i, (url, match) in enumerate(matches.items()):
            output_strings.append(f"\nKeyword {i+1}: {match['keyword']}\n")
            output_strings.append(f"URL {i+1}: {url}\n")
            output_strings.append(f"Sentence {i+1}: {match['location_of_link']}\n")
            output_strings.append(f"Anchor text {i+1}: {match['anchor_text']}\n")
            output_strings.append(f"Score {i+1}: {match['score']}\n")
        return output_strings
    
    def _process_matches(self, text, matches_found, keyword_variations, url, used_urls):
        """
        Process the matches found by the PhraseMatcher.
        """
        matches = defaultdict(lambda: {'score': 0.0, 'match': None, 'location_of_link': 'N/A', 'anchor_text': 'N/A', 'keyword': 'N/A'})
        used_anchors = set()
        potential_links = defaultdict(lambda: {'anchor': None, 'score': 0.0, 'location_of_link': 'N/A'})
        found_matches_set = set()
        location_of_link = ""
        suggestion_data = {}

        for match_id, start, end in matches_found:
            if (start, end) not in found_matches_set:
                anchor_text, location_of_link = self._extract_anchor_text_and_location(text, start, end)
                similarity_score = self._calculate_similarity_score(text, start, end, keyword_variations)
                
                if anchor_text and not anchor_text in used_anchors:
                    suggestion_data, potential_links, used_urls = self._update_suggestions(anchor_text, location_of_link, similarity_score, keyword_variations, matches, potential_links, url, used_urls)

                used_anchors.add(anchor_text)

        return matches, used_anchors, potential_links, location_of_link, suggestion_data
    
    def _extract_anchor_text_and_location(self, text, start, end):
        for sent in text.sents:
            if start >= sent.start and end <= sent.end:
                location_of_link = sent.text.strip()
                anchor_text = self._refine_anchor_text(text, start, end, sent)
                return anchor_text, location_of_link
        return "", ""

    def _refine_anchor_text(self, text, start, end, sent):
        # Refine anchor text logic
        start_index = max(start - 2, sent.start)
        end_index = min(end + 2, sent.end)
        
        for chunk in text.noun_chunks:
            if start >= chunk.start and end <= chunk.end:
                start_index = chunk.start
                end_index = chunk.end
                break

        anchor_text = text[start_index:end_index].text
        anchor_text = re.sub(r'^\W+', '', anchor_text)
        anchor_text = re.sub(r'\W+$', '', anchor_text)
        
        return anchor_text

    def _calculate_similarity_score(self, text, start, end, keyword_variations):
        keyword_tokens = self.nlp(keyword_variations[-1])
        if keyword_tokens.has_vector and text[start:end].has_vector:
            return keyword_tokens.similarity(text[start:end])
        return 0.0

    def _update_suggestions(self, anchor_text, location_of_link, similarity_score, keyword_variations, matches, potential_links, url, used_urls):
        clean_location_of_link = location_of_link
        location_of_link = location_of_link.replace(anchor_text, f"*{anchor_text}*", 1)
        suggestion_data = {
            "anchor_text": anchor_text,
            "location_of_link": location_of_link.strip(),
            "clean_location_of_link": clean_location_of_link.strip(),
            "score": similarity_score,
            "keyword": keyword_variations,
        }

        if similarity_score > matches[url]['score']:
            matches[url] = {
                'location_of_link': location_of_link,
                'location_of_link_clean': clean_location_of_link,
                'score': similarity_score,
                'anchor_text': anchor_text,
                'keyword': keyword_variations,
            }
            potential_links[url] = {
                'anchor': anchor_text,
                'score': similarity_score,
                'location_of_link': location_of_link,
                'clean_location_of_link': clean_location_of_link,
                "keyword": keyword_variations,
            }
            used_urls.add(url)

        return suggestion_data, potential_links, used_urls

    def _insert_fallback_sentence(self, text, keyword, url):
        return text, {}

    def _clean_text(self, text):
        clean_text = re.sub(r"#.*", "", text)
        clean_text = re.sub(r"\*\*.*?\*\*", "", clean_text)
        clean_text = re.sub(r"!\[.*?\]\(.*?\)", "", clean_text)
        clean_text = re.sub(r"\[.*?\]\(.*?\)", "", clean_text)
        clean_text = re.sub(r"^\s*[-*]\s.*", "", clean_text, flags=re.MULTILINE)
        clean_text = re.sub(r"<table.*?>.*?</table>", "", clean_text, flags=re.DOTALL)
        clean_text = re.sub(r"---.*?---", "", clean_text, flags=re.DOTALL)
        return clean_text


    def generate_link_suggestions_file(self):
        suggestions = {}
        
        for filename in os.listdir(self.input_directory):
            if filename.endswith(".md"):
                filepath = os.path.join(self.input_directory, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                potential_links = self.find_places_for_links(content, self.keywords_data, filepath)
                if potential_links:
                    suggestions[filename] = potential_links

        # Write suggestions to a file
        with open('suggestions.txt', 'w', encoding='utf-8') as file:
            for filename, links in suggestions.items():
                for sentence, suggestion_detail in links.items():
                    file.write(f"Link from: {filename}\n")
                    file.write(f"Link to: {suggestion_detail['link_filename']}\n")
                    file.write(f"Keyword: {suggestion_detail['data']['keyword']}\n")
                    anchor_text = suggestion_detail["data"]["anchor_text"]
                    location_of_link = suggestion_detail["data"]["location_of_link"]
                    
                    file.write(f"Anchor text: {anchor_text}\n")
                    file.write(f"Paragraph text: {location_of_link}\n")
                    file.write("\n\n")

        # now lets create a CSV file for the suggestions
        with open('suggestions.csv', 'w', encoding='utf-8') as file:
            file.write("Link from,Link to,Keywords,Anchor text,Paragraph text\n")
            for filename, links in suggestions.items():
                for sentence, suggestion_detail in links.items():
                    # convert keywords to pipe delimited string
                    keywords = suggestion_detail['data']['keyword']
                    keywords = '|'.join(keywords)
                    file.write(f"{filename},")
                    file.write(f"{suggestion_detail['link_filename']},")
                    file.write(f"{keywords},")
                    anchor_text = suggestion_detail["data"]["anchor_text"]
                    location_of_link = suggestion_detail["data"]["location_of_link"]
                    
                    file.write(f"{anchor_text},")
                    file.write(f"\"{location_of_link}\"\n")



    def insert_internal_links(self):
        for filename in os.listdir(self.input_directory):
            if filename.endswith(".md"):
                input_path = os.path.join(self.input_directory, filename)
                output_path = os.path.join(self.output_directory, filename)
                with open(input_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                

                potential_links = self.find_places_for_links(content, self.keywords_data, input_path)

                if not potential_links:
                    continue

                links = []
                for anchor_text, link_data in potential_links.items():
                    location = link_data["data"]["clean_location_of_link"]
                    link_filename = link_data["link_filename"]
                    url = self.get_url_for_filename(link_filename)
                    link = f"[{anchor_text}]({url})"
                    location_position = content.find(location)
                    anchor_position = content.find(anchor_text, location_position)
                    if anchor_position == -1:
                        continue
                    links.append((anchor_position, anchor_text, link))

                    # Inserting links into the content
                for position, anchor_text, link in sorted(links, reverse=True, key=lambda x: x[0]):
                    content = content[:position] + link + content[position + len(anchor_text):]
                
                # Saving the updated content with internal links to output directory
                with open(output_path, 'w+', encoding='utf-8') as file:
                    file.write(content)

    def get_url_for_filename(self, filename):
        """
        - Drops the .md extension from the filename
        - Adds the prefix and ends with a slash
        """
        return f"{self.prefix}/{filename[:-3]}/"

    def get_vector_representation(self, text):
        """Get the average word vector for a given text."""
        doc = self.nlp(text)
        return doc.vector

    def cosine_similarity(self, vec_a, vec_b):
        """Calculate the cosine similarity between two vectors."""
        norm_a = norm(vec_a)
        norm_b = norm(vec_b)
        
        # Check for zero vectors
        if norm_a == 0 and norm_b == 0:
            return 1.0
        if norm_a == 0 or norm_b == 0:
            return 0.0
        
        return dot(vec_a, vec_b) / (norm_a * norm_b)

    def is_semantically_similar(self, anchor_text, keywords, threshold=0.8):
        """
        Check if the anchor text is semantically similar to the target keyword.
        """
        for keyword in keywords:            
            anchor_vector = self.get_vector_representation(anchor_text.lower())
            keyword_vector = self.get_vector_representation(keyword.lower())
            
            similarity = self.cosine_similarity(anchor_vector, keyword_vector)

            if similarity >= threshold:
                return True
            
        return False

if __name__ == "__main__":
    try:
        input_directory = os.getenv('INPUT_DIR')
        if not os.path.isdir(input_directory):
            raise Exception
    except:
        print("Error: Please provide a valid input directory path in the .env file")
        sys.exit(1)

    try:
        output_directory = os.getenv('OUTPUT_DIR')
        if not os.path.isdir(output_directory):
            raise Exception
    except:
        print("Error: Please provide a valid output directory path in the .env file")
        sys.exit(1)

    linker = InternalLinker(input_directory, output_directory)

    if '-suggest' in sys.argv:
        linker.generate_link_suggestions_file()
    else:
        linker.insert_internal_links()
    print("Done!")

