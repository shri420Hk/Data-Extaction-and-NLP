<<<<<<< HEAD
INSTRUCTIONS:
Approach to the Solution:
Problem Understanding:

The task involves extracting article text from given URLs, conducting textual analysis, and saving results in a structured output format.
Textual analysis includes sentiment analysis, counting complex words, calculating Fog Index, and other specified metrics.
Solution Components:

Utilized BeautifulSoup for web scraping, NLTK and TextBlob for NLP, and Pandas for data manipulation and output handling.
Created functions for sentiment analysis, word counting, Fog Index calculation, and other textual analysis tasks.

RESOURCE MANAGEMENT:
Loaded negative and positive words, stopwords, and extracted resources from provided zip files.
Adjusted parameters based on the analysis document and input data.

OUTPUT HANDLING:
Saved individual text files for each article.
Stored analysis results in a structured CSV file.
How to Run the .py File to Generate Output:

ISTALL DEPENDENCIES:
Ensure Python is installed on your system.
Install required packages by running:
pip install -r requirements.txt
Download Resources:
Download and extract the two provided zip files: MasterDictionary-20240227T095609Z-001.zip and StopWords-20240227T095658Z-001.zip.
Adjust paths in the script accordingly.

RUN THE SCRIPT:
Open a terminal and navigate to the script's directory.
Execute the script using the command:
bash
Copy code
python3 text_analysis_script.py

REVIEW OUTPUT:
The script will generate individual text files for each article, and analysis results will be stored in output.csv.

ADDITIONAL NOTES:
Ensure correct file paths are used for resources and input data.
Adjust paths and URLs as needed for your specific use case.
Be mindful of permissions for file writing in specified directories.

DEPENDENCIES:
BeautifulSoup: Used for web scraping.
NLTK: Natural Language Toolkit for NLP tasks.
TextBlob: Library for processing textual data.
Pandas: Data manipulation and CSV handling.
=======
#Data Extraction and Text Analysis Program

#Introduction

This Python program is designed to extract textual data from articles on a website, as specified in the assignment. The objective is to perform text analysis and compute various variables outlined in the "Text Analysis.docx" document.

#Prerequisites

Python 3.x
Required Python packages: BeautifulSoup, requests, openpyxl, nltk
Install the required packages using the following command:

bash

Copy code

pip install beautifulsoup4 
requests openpyxl nltk

#Usage
Clone the repository to your local machine.
Place the Input.xlsx file with the list of articles in the same directory as the script.
Run the Python script:

bash

Copy code

python new.py
#Input

The program takes input from the provided Input.xlsx file, which contains a list of articles.


#Output

For each article, the program extracts the article title and text, saving it in a text file with the format URL_ID.txt.

Text Analysis
The definition of each variable for text analysis can be found in the "Text Analysis.docx" file. The program performs analysis on the extracted articles and computes the following variables:

POSITIVE SCORE
NEGATIVE SCORE
POLARITY SCORE
SUBJECTIVITY SCORE
AVG SENTENCE LENGTH
PERCENTAGE OF COMPLEX WORDS
FOG INDEX
AVG NUMBER OF WORDS PER SENTENCE
COMPLEX WORD COUNT
WORD COUNT
SYLLABLE PER WORD
PERSONAL PRONOUNS
AVG WORD LENGTH
Note
While extracting text, the program ensures that only the article title and text are included, excluding any website headers, footers, or other unnecessary information.

Author
shri420Hk

Feel free to reach out for any questions or improvements!
>>>>>>> b337a8ade5d31abf4bf0fb3a88f39f93814f3d2b
