# this is using the built in map functionality in Python
# because our group ony has two members
import collections
from collections import Counter, defaultdict

# imports Natural Language Tool Kit popular package
import nltk
import math
import re
import os
from zipfile import ZipFile
from nltk import WordNetLemmatizer
import hash
nltk.download("stopwords")


def tfidf(input_word, words, file_count):
    tfidf_dict = {}
    # tf = # of times word appears in document / total number of words in document
    if input_word in words:
        films = words[input_word]
    # make sure word in map
    else:
        print("Word not found.")
        return
    for film, freq, total in films:
        tf = freq / total
        # idf = log(# of documents / # of documents that contain term)
        idf = math.log10(file_count / len(films))
        tfidf_dict[film] = (tf * idf)

    # print top scoring tf-idfs
    print("Top Scorers: ")
    sorted_tf_idf = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)
    for count, (film, tf_idf) in enumerate(sorted_tf_idf):
        if count < 5:
            print(f"({count + 1}). {film}: {tf_idf:.2e}")


def main():
    words = defaultdict(list)
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append(',')
    print("Loading data...")
    # for all the files or a section of the files (it's a lot of data)
    for x in range(1, 2):
        # formula for file name
        file_name = f"data/movie scripts {x}.zip"
        # open zip file
        with ZipFile(file_name, "r") as zip_file:
            # number of documents
            file_count = 0
            # open each doc in each folder
            for file_name in zip_file.namelist():
                file_count += 1
                with zip_file.open(file_name) as file:
                    # find film title from doc name
                    film_title = re.search("\/[ a-z A-Z 0-9]+_", file_name).group()
                    file_content = file.read().decode("utf-8")
                    word_count = 0
                    # list of words
                    word_list = []
                    for word in file_content.split():
                        if word in stopwords:
                            word_count += 1
                        else:
                            word_count += 1
                            word_list.append(word.lower())
                    count = Counter(word_list)
                    for word, num in count.most_common():
                        words[word].append((film_title[1:-1], num, len(word_list)))
    # make sure dict/map is ordered
    words = collections.OrderedDict(sorted(words.items()))
    print('Data loaded')
    # lemmatize user input
    lemmatizer = WordNetLemmatizer()
    user_word = input('Enter word to be analyzed (0 to exit): ')
    # go until input is 0
    while user_word != "0":
        tfidf(lemmatizer.lemmatize(user_word), words, file_count)
        user_word = input('Enter word to be analyzed (0 to exit): ')


if __name__ == "__main__":
    main()