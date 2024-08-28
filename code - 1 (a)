
from collections import Counter
import matplotlib.pyplot as plt

#File 1

with open("/content/en_hi_gov_all.txt", 'r', encoding='utf-8') as f:
    text = f.read()
text_list = text.split("\n")
print(text_list)
lang1_sen = []
lang2_sen = []
for line in text_list:
    sentences = line.split("\t")
    for i in range(len(sentences)):
      if i%2 == 1:
        lang1_sen.append(sentences[i])
      else:
        lang2_sen.append(sentences[i])
print(lang1_sen)
print(lang2_sen)

#File 2

with open("/content/en_hi_hlt_all.txt", 'r', encoding='utf-8') as f:
    text = f.read()
text_list = text.split("\n")
print(text_list)
lang1_sen = []
lang2_sen = []
for line in text_list:
    sentences = line.split("\t")
    for i in range(len(sentences)):
      if i%2 == 1:
        lang1_sen.append(sentences[i])
      else:
        lang2_sen.append(sentences[i])
print(lang1_sen)
print(lang2_sen)

#File 3

with open("/content/hi_en_gov_all.txt", 'r', encoding='utf-8') as f:
    text = f.read()
text_list = text.split("\n")
print(text_list)
lang1_sen = []
lang2_sen = []
for line in text_list:
    sentences = line.split("\t")
    for i in range(len(sentences)):
      if i%2 == 0:
        lang1_sen.append(sentences[i])
      else:
        lang2_sen.append(sentences[i])
print(lang1_sen)
print(lang2_sen)

#File 4

with open("/content/hi_en_hlt_all.txt", 'r', encoding='utf-8') as f:
    text = f.read()
text_list = text.split("\n")
print(text_list)
lang1_sen = []
lang2_sen = []
for line in text_list:
    sentences = line.split("\t")
    for i in range(len(sentences)):
      if i%2 == 0:
        lang1_sen.append(sentences[i])
      else:
        lang2_sen.append(sentences[i])
print(lang1_sen)
print(lang2_sen)

#All Combined

file_paths = [
    "/content/en_hi_gov_all.txt",
    "/content/en_hi_hlt_all.txt",
    "/content/hi_en_gov_all.txt",
    "/content/hi_en_hlt_all.txt"
]
lang1_sen = []
lang2_sen = []
for index, file_path in enumerate(file_paths):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    text_list = text.split("\n")
    for line in text_list:
        sentences = line.split("\t")
        if index < 2:
            for i in range(len(sentences)):
                if i % 2 == 1:
                    lang1_sen.append(sentences[i])
                else:
                    lang2_sen.append(sentences[i])
        else:
            for i in range(len(sentences)):
                if i % 2 == 0:
                    lang1_sen.append(sentences[i])
                else:
                    lang2_sen.append(sentences[i])
print("Language 1 Sentences:", lang1_sen)
print("Language 2 Sentences:", lang2_sen)

#Plotting

def get_word_frequencies(sentences):
    words = []
    for sentence in sentences:
        words.extend(sentence.split())
    return Counter(words)
lang1_word_freq = get_word_frequencies(lang1_sen)
lang2_word_freq = get_word_frequencies(lang2_sen)
def plot_word_frequency(word_freq, language_name):
    most_common_words = word_freq.most_common(10)
    words, frequencies = zip(*most_common_words) if most_common_words else ([], [])
    plt.figure(figsize=(10, 5))
    plt.bar(words, frequencies)
    plt.title(f"Top 10 Most Common Words in {language_name}")
    plt.xlabel("Words")
    plt.ylabel("Frequencies")
    plt.xticks(rotation=45)
    plt.show()
plot_word_frequency(lang1_word_freq, "Language 1")
plot_word_frequency(lang2_word_freq, "Language 2")
