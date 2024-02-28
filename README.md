#Data Extraction and Text Analysis Program

#Introduction

This Python program is designed to extract textual data from articles on a website, as specified in the assignment. The objective is to perform text analysis and compute various variables outlined in the "Text Analysis.docx" document.

Prerequisites

Python 3.x
Required Python packages: BeautifulSoup, requests, openpyxl, nltk
Install the required packages using the following command:

bash
Copy code
pip install beautifulsoup4 requests openpyxl nltk
Usage
Clone the repository to your local machine.
Place the Input.xlsx file with the list of articles in the same directory as the script.
Run the Python script:
bash
Copy code
python data_extraction_and_analysis.py
Input
The program takes input from the provided Input.xlsx file, which contains a list of articles.

Output
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

License
This program is licensed under the MIT License - see the LICENSE file for details.

Author
shri420Hk

Feel free to reach out for any questions or improvements!
