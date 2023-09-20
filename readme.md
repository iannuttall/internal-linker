# Internal Linker

This is a WIP internal linking project that extracts keywords from a folder of Markdown files, and uses that list to find relevant internal links to insert.

## Prerequisites

I use pipenv to manage my virtual environments. If you don't have it, you can find info on how to install it [here](https://pipenv.pypa.io/en/latest/installation/).

If you are using a different virtual environment manager, you can use the `requirements.txt` file to install the dependencies:

```
pip install -r requirements.txt
```

Make sure you rename the .env-example file to .env and add the correct paths to your input and output folders. By default, these are set to the input and output folders in this repo so you can test it out.

Also make sure to install the en_core_web_md model for spaCy:

```
pipenv run python -m spacy download en_core_web_md
```

If you're not using pipenv, from your virtual environment, run:

```
python -m spacy download en_core_web_md
```

## Usage

I have included a few articles from [Practical Programmatic](https://practicalprogrammatic.com) in the `input` folder.

You can generate a keywords.txt file to see what keywords are extracted from articles in this folder by running:

```
pipenv run python keywords.py
```

To get internal link suggestions exported to suggestions.csv and suggestions.txt, run the following command:

```
pipenv run python links.py -suggest
```

If you want to actually insert the links and save to the output folder, run:

```
pipenv run python links.py
```

## Contributing

If you have any suggestions or ideas for improving this to make the internal linking suggestions more accurate, you can fork this repo and submit a pull request. I would love to hear your ideas!