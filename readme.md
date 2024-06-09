Word Frequency Analysis from PDF Texts
# Overview

This Python script analyzes the word frequency distribution of texts extracted from PDF files. It calculates the total word count, identifies the top 20 most frequent words, and generates visualizations to analyze whether the word frequency distribution follows Zipf's Law and Pareto Distribution. Additionally, it saves the word frequency data to a CSV file for further analysis.

# Features

    Extracts text from PDF files.
    Cleans the text by removing non-alphanumeric characters and converting to lowercase.
    Computes the total word count and frequency of each word.
    Identifies the top 20 most frequent words.
    Generates bar charts for visualizing word frequency.
    Performs analysis to determine compliance with Zipf's Law and Pareto Distribution.
    Saves word frequency data to a CSV file.
    Creates separate folders for each book, containing analysis results and CSV files.

# Requirements

    Python 3.x
    PyPDF2
    Matplotlib

# Usage

    Clone the repository or download the script.
    Install the required dependencies using pip:

    pip install PyPDF2 matplotlib

Place your PDF files in the same directory as the script.
Update the BOOK_TITLES variable in the script with the names of your PDF files.
Run the script:

    python3 main.py

    The script will generate analysis results, visualizations, and CSV files for each PDF file in separate folders.

# Analysis Results

    Total Word Count: Provides the total number of words in the text.
    Top 20 Most Frequent Words: Lists the 20 most frequently occurring words and their frequencies.
    Zipf's Law Analysis: Visualizes the word frequency distribution to determine compliance with Zipf's Law.
    Pareto Distribution Analysis: Visualizes the cumulative word frequency to assess compliance with Pareto Distribution.

# Output

The script generates the following files for each PDF:

    {book_title}_stdout.txt: Contains analysis results and information printed during script execution.
    {book_title}_word_frequency.png: Bar chart visualizing the top 20 word frequencies.
    {book_title}_zipf_analysis.png: Plot for analyzing compliance with Zipf's Law.
    {book_title}_pareto_analysis.png: Plot for analyzing compliance with Pareto Distribution.
    word_frequency.csv: CSV file containing all words and their frequencies.

# License

This project is licensed under the MIT License.
