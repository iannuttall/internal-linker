import os
import sys
import spacy
import yake
import math
import nltk
from collections import defaultdict
from nltk.corpus import wordnet
from dotenv import load_dotenv
load_dotenv()
# nltk.download('wordnet')

class KeywordExtractor:

    def __init__(self, directory_path):
        self.nlp = spacy.load("en_core_web_md")

        self.language = "en"
        self.max_ngram_size = 3
        self.deduplication_threshold = 0.7
        self.num_of_keywords = 10
        self.custom_kw_extractor = yake.KeywordExtractor(
            lan=self.language, 
            n=self.max_ngram_size, 
            dedupLim=self.deduplication_threshold, 
            top=self.num_of_keywords, 
            features=None
        )

        self.directory_path = directory_path
        self.df_dict = defaultdict(int)
        self.total_documents = 0

        self._build_df_dict()

    def _build_df_dict(self):
        for filename in os.listdir(self.directory_path):
            if filename.endswith(".md"):
                with open(os.path.join(self.directory_path, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    keywords = self._extract_raw_keywords_from_text(content)
                    unique_keywords = set(keywords)
                    for kw in unique_keywords:
                        self.df_dict[kw] += 1

        self.total_documents = len(os.listdir(self.directory_path))

    def _extract_raw_keywords_from_text(self, text):
        keywords = self.custom_kw_extractor.extract_keywords(text)
        return [kw[0] for kw in keywords]

    def _calculate_idf(self, term):
        df_t = self.df_dict.get(term, 0)
        idf_smoothed = math.log((self.total_documents + 1) / (df_t + 1)) + 1
        return idf_smoothed


    def _extract_frontmatter(self, text):
        if text.startswith('---'):
            end_of_frontmatter = text.split('---', 2)[1]
            frontmatter_lines = [line.strip() for line in end_of_frontmatter.split('\n') if line.strip()]
            frontmatter = {}
            for line in frontmatter_lines:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"')
            return frontmatter
        return {}
    
    def get_synonyms(self, word):
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace("_", " "))
        return list(synonyms)

    def extract_keywords_from_text(self, text):
        keywords = self.custom_kw_extractor.extract_keywords(text)
        frontmatter = self._extract_frontmatter(text)
        h1_tag = frontmatter.get('h1', '').lower()
        description = frontmatter.get('description', '').lower()

        h1_tokens = self.nlp(h1_tag)
        description_tokens = self.nlp(description)

        h1_keyword_multiplier = 0.00005
        description_keyword_multiplier = 0.025
        direct_substring_multiplier = 0.0001

        for idx, (kw, score) in enumerate(keywords):
            kw_tokens = self.nlp(kw)
            kw_lower = kw.lower()
            
            # Check if keyword is a direct substring of the title
            if kw_lower in h1_tag:
                score *= direct_substring_multiplier
                # If the keyword has multiple words and matches the title, give it a stronger boost
                if len(kw_lower.split()) > 1:
                    score *= direct_substring_multiplier

            h1_similarity = max([token1.similarity(token2) for token1 in kw_tokens for token2 in h1_tokens if token1.has_vector and token2.has_vector], default=0)
            desc_similarity = max([token1.similarity(token2) for token1 in kw_tokens for token2 in description_tokens if token1.has_vector and token2.has_vector], default=0)

            similarity_threshold = 0.95

            if h1_similarity > similarity_threshold:
                score *= h1_keyword_multiplier
            elif desc_similarity > similarity_threshold:
                score *= description_keyword_multiplier
            
            idf_value = self._calculate_idf(kw)
            score *= idf_value

            keywords[idx] = (kw, score)

        # Sort keywords based on score (lower scores first due to how we've adjusted the multipliers)
        sorted_keywords = sorted(keywords, key=lambda x: x[1])
        return {kw[0]: kw[1] for kw in sorted_keywords}

    def _remove_common_keywords(self, keywords_data):
        common_keywords = set()
        
        # Calculate threshold
        threshold = 0.50 * self.total_documents

        for keyword, frequency in self.df_dict.items():
            if frequency > threshold:
                common_keywords.add(keyword)

        # Remove common keywords from keywords_data
        for filename, keywords in keywords_data.items():
            filtered_keywords = {kw: score for kw, score in keywords.items() if kw not in common_keywords}
            keywords_data[filename] = filtered_keywords

        return keywords_data

    def extract_keywords_for_directory(self):
        keywords_data = {}

        for filename in os.listdir(self.directory_path):
            if filename.endswith(".md"):
                with open(os.path.join(self.directory_path, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    keywords = self.extract_keywords_from_text(content)
                    keywords_data[filename] = keywords
        
        # After extracting keywords, remove common ones
        keywords_data = self._remove_common_keywords(keywords_data)

        # keep top 3 keywords only
        for filename, keywords in keywords_data.items():
            top_keywords = dict(sorted(keywords.items(), key=lambda item: item[1])[:3])
            keywords_data[filename] = top_keywords

        return keywords_data
    
def get_keywords_for_folder(directory_path):
    extractor = KeywordExtractor(directory_path)
    return extractor.extract_keywords_for_directory()

if __name__ == "__main__":
    try:
        directory_path = os.getenv('INPUT_DIR')
        if not os.path.isdir(directory_path):
            raise Exception
    except:
        print("Error: Please provide a valid input directory path in the .env file")
        sys.exit(1)

    extractor = KeywordExtractor(directory_path)
    keywords_data = extractor.extract_keywords_for_directory()

    with open('keywords.txt', 'w', encoding='utf-8') as file:
        for filename, keywords in keywords_data.items():
            keywords_str = ', '.join([f'"{keyword}": {score}' for keyword, score in keywords.items()])
            file.write(f'{filename}\n {{{keywords_str}}}\n\n')

