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
