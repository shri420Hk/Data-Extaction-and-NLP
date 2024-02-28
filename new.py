import requests
from bs4 import BeautifulSoup
import nltk
from textblob import TextBlob  # Ensure you have TextBlob installed: pip install textblob
import pandas as pd
import re
import os
import zipfile

# Download NLTK resources
nltk.download('punkt')

# Load negative and positive words
def load_sentiment_words(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        words = file.read().splitlines()
    return words

# Load stopwords
def load_stopwords(folder_path):
    stopwords = set()
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), 'r', encoding='ISO-8859-1') as file:
            stopwords.update(file.read().splitlines())
    return stopwords

# Extract resources from zip files
def extract_resources(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Function to extract article text from URL
def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust the selector based on the structure of the HTML in the articles
    paragraphs = soup.find_all('p')

    # Combine paragraphs to form the article text
    article_text = ' '.join([paragraph.get_text() for paragraph in paragraphs])

    return article_text

# Function to count complex words
def count_complex_words(words):
    return sum(1 for word in words if len(word) > 6)  # Adjust the condition based on your definition of complex words

# Function to calculate Fog Index
def calculate_fog_index(avg_sentence_length, percentage_complex_words):
    return 0  # Replace with your Fog Index calculation logic

# Function to count syllables in a word
def count_syllables(word):
    if isinstance(word, str):
        return max(1, len(re.findall(r'[aeiouy]+', word, flags=re.IGNORECASE)))
    return 1  # Default to 1 syllable for non-string elements

# Function to count personal pronouns
def count_personal_pronouns(words):
    personal_pronouns = ['I', 'me', 'my', 'mine', 'myself', 'you', 'your', 'yours', 'yourself', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'we', 'us', 'our', 'ours', 'ourselves', 'they', 'them', 'their', 'theirs', 'themselves']
    return sum(1 for word in words if word.lower() in personal_pronouns)

# Function to perform textual analysis and compute variables
def perform_textual_analysis(article_text, positive_words, negative_words):
    # Tokenize sentences
    sentences = nltk.sent_tokenize(article_text)

    # Tokenize words
    words = nltk.word_tokenize(article_text)

    # Calculate percentage of complex words
    percentage_complex_words = (count_complex_words(words) / len(words)) * 100

    # Calculate Fog Index
    fog_index = calculate_fog_index(len(words) / len(sentences), percentage_complex_words)

    # Calculate average number of words per sentence
    avg_words_per_sentence = len(words) / len(sentences)

    # Calculate syllables per word
    syllables_per_word = sum(count_syllables(word) for word in words) / len(words)

    # Count personal pronouns
    personal_pronoun_count = count_personal_pronouns(words)

    # Perform sentiment analysis using additional resources
    positive_score = sum(1 for word in words if word.lower() in positive_words)
    negative_score = sum(1 for word in words if word.lower() in negative_words)

    # Other variables as per the analysis document
    complex_word_count = count_complex_words(words)
    word_count = len(words)
    avg_word_length = sum(len(word) for word in words) / len(words)

    return {
        'POSITIVE SCORE': positive_score,
        'NEGATIVE SCORE': negative_score,
        'POLARITY SCORE': positive_score - negative_score,
        'SUBJECTIVITY SCORE': 1 - abs(positive_score - negative_score),  # Adjusting for a more intuitive scale
        'AVG SENTENCE LENGTH': len(words) / len(sentences),
        'PERCENTAGE OF COMPLEX WORDS': percentage_complex_words,
        'FOG INDEX': fog_index,
        'AVG NUMBER OF WORDS PER SENTENCE': avg_words_per_sentence,
        'COMPLEX WORD COUNT': complex_word_count,
        'WORD COUNT': word_count,
        'SYLLABLE PER WORD': syllables_per_word,
        'PERSONAL PRONOUNS': personal_pronoun_count,
        'AVG WORD LENGTH': avg_word_length
    }

# Load resources
master_dict_path = "/home/srikant/Pictures/blackcoffer/MasterDictionary-20240227T095609Z-001/MasterDictionary"
negative_words = load_sentiment_words(os.path.join(master_dict_path, "negative-words.txt"))
positive_words = load_sentiment_words(os.path.join(master_dict_path, "positive-words.txt"))

stopwords_path = "/home/srikant/Pictures/blackcoffer/StopWords-20240227T095658Z-001/StopWords/"
stopwords = load_stopwords(stopwords_path)

# Extract resources from zip files
extract_resources("/home/srikant/Pictures/blackcoffer/MasterDictionary-20240227T095609Z-001.zip", "/home/srikant/Pictures/blackcoffer")
extract_resources("/home/srikant/Pictures/blackcoffer/StopWords-20240227T095658Z-001.zip", "/home/srikant/Pictures/blackcoffer")

# Read input file
input_df = pd.read_excel('/home/srikant/Pictures/blackcoffer/Input.xlsx')

# Output DataFrame
output_columns = ['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
                  'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
                  'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT',
                  'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']

# Iterate through each row in the input dataframe
for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    article_url = row['URL']

    # Extract article text from the URL
    article_text = extract_article_text(article_url)

    # Perform textual analysis
    analysis_results = perform_textual_analysis(article_text, positive_words, negative_words)

    # Save the extracted article text to a file
    with open(f'/home/srikant/Pictures/blackcoffer/{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(article_text)

    # Create a dictionary with URL_ID, URL, and analysis results
    output_data = {'URL_ID': url_id, 'URL': article_url, **analysis_results}

    # Save the output data to a CSV file
    output_df = pd.DataFrame([output_data], columns=output_columns)
    output_df.to_csv('/home/srikant/Pictures/blackcoffer/output.csv', mode='a', header=not bool(index), index=False)
