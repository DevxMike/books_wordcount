import os
import sys
import PyPDF2
import re
from collections import Counter
import matplotlib.pyplot as plt
import csv

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

def clean_text(text):
    cleaned_text = re.sub(r'\W+', ' ', text) 
    cleaned_text = cleaned_text.lower()  
    return cleaned_text

def generate_word_statistics(text):
    words = text.split()
    words = [word for word in words if len(word) > 3]
    word_count = len(words)
    word_frequency = Counter(words)
    return word_count, word_frequency

def plot_top_word_frequency(word_frequency, book_title, folder):
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
    top_words = list(sorted_word_frequency.keys())[:20]
    frequencies = list(sorted_word_frequency.values())[:20]
    plt.figure(figsize=(10, 6))
    plt.bar(top_words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 20 Word Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(folder, f'{book_title}_top_word_frequency.png'))
    plt.close()

def plot_all_word_frequency(word_frequency, book_title, folder):
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
    ranks = list(range(1, len(sorted_word_frequency) + 1))
    max_frequency = max(sorted_word_frequency.values())
    plt.figure(figsize=(10, 6))
    plt.bar(ranks, sorted_word_frequency.values(), color='skyblue')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Distribution')
    plt.ylim(0, max_frequency)
    plt.tight_layout()
    plt.savefig(os.path.join(folder, f'{book_title}_word_frequency_distribution.png'))
    plt.close()

def zipf_analysis(word_frequency, book_title, folder):
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
    ranks = list(range(1, len(sorted_word_frequency) + 1))
    frequencies = list(sorted_word_frequency.values())
    plt.plot(ranks, frequencies, marker='o', linestyle='-', color='b')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Zipf Law Analysis')
    plt.tight_layout()
    plt.savefig(os.path.join(folder, f'{book_title}_zipf_analysis.png'))
    plt.close()
    if all(frequencies[i] >= frequencies[i+1] for i in range(len(frequencies)-1)):
        zipf_result = "Prawo Zipfa jest spełnione."
    else:
        zipf_result = "Prawo Zipfa nie jest spełnione."
    return zipf_result

def pareto_analysis(word_frequency, book_title, folder):
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
    frequencies = list(sorted_word_frequency.values())
    cumulative_frequency = [sum(frequencies[:i+1]) for i in range(len(frequencies))]
    plt.plot(range(1, len(frequencies) + 1), cumulative_frequency, marker='o', linestyle='-', color='r')
    plt.xlabel('Rank')
    plt.ylabel('Cumulative Frequency')
    plt.title('Pareto Distribution Analysis')
    plt.tight_layout()
    plt.savefig(os.path.join(folder, f'{book_title}_pareto_analysis.png'))
    plt.close()
    if all(cumulative_frequency[i] >= cumulative_frequency[i-1] for i in range(1, len(cumulative_frequency))):
        pareto_result = "Rozkład Pareto jest spełniony."
    else:
        pareto_result = "Rozkład Pareto nie jest spełniony."
    return pareto_result

def create_folder(book_title):
    folder = book_title.split('.')[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def write_csv(word_frequency, folder):
    csv_file = os.path.join(folder, 'word_frequency.csv')
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Frequency'])
        for word, frequency in word_frequency.items():
            writer.writerow([word, frequency])

def main():
    BOOK_TITLES = ('kucharz.pdf', 'maklowicz.pdf', 'baltyckie.pdf')  
    for book_title in BOOK_TITLES:
        folder = create_folder(book_title)
        stdout_file = os.path.join(folder, f'{book_title}_stdout.txt')
        with open(stdout_file, 'w') as stdout:
            sys.stdout = stdout
            file_path = book_title
            text = read_pdf(file_path)
            cleaned_text = clean_text(text)
            word_count, word_frequency = generate_word_statistics(cleaned_text)
            print(f"Total word count for {book_title}: {word_count}")
            print("Top 20 most frequent words:")
            for word, frequency in word_frequency.most_common(20):
                print(f"{word}: {frequency}")
            plot_top_word_frequency(word_frequency, book_title, folder)
            plot_all_word_frequency(word_frequency, book_title, folder)
            zipf_result = zipf_analysis(word_frequency, book_title, folder)
            pareto_result = pareto_analysis(word_frequency, book_title, folder)
            print(zipf_result)
            print(pareto_result)
            write_csv(word_frequency, folder)
            sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
