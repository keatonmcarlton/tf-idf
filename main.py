# imports Natural Language Tool Kit popular package
import re
from zipfile import ZipFile

import nltk
import os

from nltk import WordNetLemmatizer

import hash
nltk.download("stopwords")
stopwords = set(nltk.corpus.stopwords.words("english"))


def tfidf(hash_table, word_count_dictionary, word, number_to_name_dict):
    tfidf_dict = {}
    for i, word_count in word_count_dictionary.items():
        idf = hash_table.get(word).idf()
        # tf = # of times word appears in document / total number of words in document
        tf = hash_table.get(word).script[i] / word_count
        # tf-idf = tf * idf
        tfidf_dict[number_to_name_dict[i]] = tf * idf
    tfidf_dict = dict(sorted(tfidf_dict.items(), key=lambda guy: guy[1], reverse=True))
    print("Top scorers:")
    count = 1
    for name, score in tfidf_dict.items():
        if count < 6 and score != 0:
            print(f"({count}). {name}: {score:.2e}")
            count += 1


def split(file_name):
    pieces = file_name.split('_', 2)
    return pieces[0], int(pieces[1])


def main():
    lemmatizer = WordNetLemmatizer()
    name_to_number_dict = {}
    number_to_name_dict = {}
    word_count_dict = {}
    movie_hash = hash.HashTable(10)

    # for all the files or just a section
    file_count = 0
    for x in range(1, 2):
        # formula for file name
        file_name = f"data/movie scripts {x}.zip"
        # open zip file
        with ZipFile(file_name, 'r') as zip_file:
            # num of docs
            # open each doc in each folder
            for file_name in zip_file.namelist():
                file_count += 1
                if file_count % 25 == 0:
                    print(file_count)
                with zip_file.open(file_name, 'r') as f:
                    film_title = re.search("\/[a-zA-Z 0-9]+_", file_name).group()
                    film_title = film_title[1:-1]
                    name_to_number_dict[film_title] = file_count
                    number_to_name_dict[file_count] = film_title
                    stuff = f.read().decode("utf-8")
                    words = stuff.split()
                    word_count_dict[file_count] = len(words)
                    for word in words:
                        if word.isalnum() and word not in stopwords:
                            break
                            #movie_hash.set_val(word, file_count)
                f.close()
    print(f"Total entries: {file_count:,}")
    exit_program = False
    while not exit_program:
        user_input = input("Enter word to be analyzed (0 to exit): ")
        if user_input == '0':
            exit_program = True
        else:
            myword = movie_hash.get(lemmatizer.lemmatize(user_input))
            if myword is not None:
                if myword.word != user_input:
                    print()
                    print(f"Your word: '{user_input}' lemmatizes to {myword.word}")
                    print()
                tfidf(movie_hash, word_count_dict, myword.word, number_to_name_dict)
            else:
                print("Didnt find that word.")
            print()
    print("\nMay take a while to exit..")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
