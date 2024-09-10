import nltk
from nltk import bigrams, trigrams
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import matplotlib.pyplot as plt

#Bigrams

filenames = [
    '/content/en_hi_gov_all.txt',
    '/content/en_hi_hlt_all.txt',
    '/content/hi_en_gov_all.txt',
    '/content/hi_en_hlt_all.txt'
]
overall_bigram_freq = Counter()
bigram_freqs = {}  
for filename in filenames:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        tokens = word_tokenize(text)
        bigrams_list = list(bigrams(tokens))
        filtered_bigrams = [
            bigram for bigram in bigrams_list if all(word not in string.punctuation for word in bigram)
        ]
        bigram_freq = Counter(filtered_bigrams)
        overall_bigram_freq.update(bigram_freq)
        bigram_freqs[filename] = bigram_freq
        most_common_bigrams = bigram_freq.most_common(10)
        print(f"\nMost common bigrams in {filename}:")
        for bigram, freq in most_common_bigrams:
            print(f"{bigram}: {freq}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
most_common_overall = overall_bigram_freq.most_common(10)
print("\nMost common bigrams across all files:")
for bigram, freq in most_common_overall:
    print(f"{bigram}: {freq}")
def plot_bigrams(bigram_freq, title):
    bigrams, freqs = zip(*bigram_freq.most_common(10))
    bigrams = [' '.join(bigram) for bigram in bigrams]
    plt.figure(figsize=(10, 6))
    plt.barh(bigrams, freqs, color='skyblue')
    plt.xlabel('Frequency')
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()
for filename, freq in bigram_freqs.items():
    plot_bigrams(freq, f'Bigrams in {filename}')
plot_bigrams(overall_bigram_freq, 'Overall Bigrams')

#Trigrams

filenames = [
    '/content/en_hi_gov_all.txt',
    '/content/en_hi_hlt_all.txt',
    '/content/hi_en_gov_all.txt',
    '/content/hi_en_hlt_all.txt'
]
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    trigrams_list = list(trigrams(tokens))
    filtered_trigrams = [
        trigram for trigram in trigrams_list if all(word not in string.punctuation for word in trigram)
    ]
    trigram_freq = Counter(filtered_trigrams)
    
    most_common_trigrams = trigram_freq.most_common(10)
    print(f"\nMost common trigrams in {filename}:")
    for trigram, freq in most_common_trigrams:
        print(f"{trigram}: {freq}")
    
    trigram_labels = [' '.join(trigram) for trigram, _ in most_common_trigrams]
    trigram_counts = [freq for _, freq in most_common_trigrams]
    plt.figure(figsize=(12, 8))
    plt.barh(trigram_labels, trigram_counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Trigrams')
    plt.title(f'Most Common Trigrams in {filename}')
    plt.gca().invert_yaxis() 
    plt.show()
overall_trigram_freq = Counter()
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    trigrams_list = list(trigrams(tokens))
    filtered_trigrams = [
        trigram for trigram in trigrams_list if all(word not in string.punctuation for word in trigram)
    ]
    trigram_freq = Counter(filtered_trigrams)
    overall_trigram_freq.update(trigram_freq)
most_common_overall = overall_trigram_freq.most_common(10)
trigram_labels = [' '.join(trigram) for trigram, _ in most_common_overall]
trigram_counts = [freq for _, freq in most_common_overall]
plt.figure(figsize=(12, 8))
plt.barh(trigram_labels, trigram_counts, color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Trigrams')
plt.title('Most Common Trigrams Across All Files')
plt.gca().invert_yaxis()
plt.show()

#Quadgrams

filenames = [
    '/content/en_hi_gov_all.txt',
    '/content/en_hi_hlt_all.txt',
    '/content/hi_en_gov_all.txt',
    '/content/hi_en_hlt_all.txt'
]
overall_quadgram_freq = Counter()
file_quadgram_freqs = {}
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    tokens = word_tokenize(text)
    quadgrams_list = list(ngrams(tokens, 4))
    filtered_quadgrams = [
        quadgram for quadgram in quadgrams_list if all(word not in string.punctuation for word in quadgram)
    ]
    quadgram_freq = Counter(filtered_quadgrams)
    overall_quadgram_freq.update(quadgram_freq)
    file_quadgram_freqs[filename] = quadgram_freq
    most_common_quadgrams = quadgram_freq.most_common(10)
    print(f"\nMost common quadgrams in {filename}:")
    for quadgram, freq in most_common_quadgrams:
        print(f"{quadgram}: {freq}")
most_common_overall = overall_quadgram_freq.most_common(10)
print("\nMost common quadgrams across all files:")
for quadgram, freq in most_common_overall:
    print(f"{quadgram}: {freq}")

for filename, quadgram_freq in file_quadgram_freqs.items():
    quadgrams, freqs = zip(*quadgram_freq.most_common(10))
    plt.figure()
    plt.barh(range(len(freqs)), freqs, color='skyblue', tick_label=[str(q) for q in quadgrams])
    plt.title(f'Most Common Quadgrams in {filename}')
    plt.xticks(rotation=90)
    plt.xlabel('Quadgram')
    plt.ylabel('Frequency')
    plt.tight_layout()
plt.figure()
overall_quadgrams, overall_freqs = zip(*most_common_overall)
plt.bar(range(len(overall_freqs)), overall_freqs, tick_label=[str(q) for q in overall_quadgrams])
plt.title('Most Common Quadgrams Across All Files')
plt.xticks(rotation=90)
plt.xlabel('Quadgram')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

