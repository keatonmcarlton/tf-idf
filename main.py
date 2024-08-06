# imports Natural Language Tool Kit popular package
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
    # this is the name of the folder that holds the text files of movie scripts
    file_folder = r"data/movie scripts 1.zip"
    num_files = 0

    for file in os.listdir(file_folder):
        num_files += 1
    movie_hash = hash.HashTable(num_files)
    running_entries_count = 0
    print("Total files loaded:")
    for i, file_name in enumerate(os.listdir(file_folder)):
        # Open file
        with open(os.path.join(file_folder, file_name), 'r', encoding='utf-8') as f:
            name, num_entries = split(file_name)
            running_entries_count += num_entries
            #some files have the same names, such as 'xmen' and 'whos your daddy' for some reason.
            #deal with this later, TODO
            name_to_number_dict[name] = i
            number_to_name_dict[i] = name
            word_count_dict[i] = num_entries
            """
            if i == 0:
                name_to_number_dict[name] = i
                number_to_name_dict[i] = name
                word_count_dict[i] = num_entries
            elif name != number_to_name_dict[i-1]:
                name_to_number_dict[name] = i
                number_to_name_dict[i] = name
                word_count_dict[i] = num_entries
            else:
                i -= 1
                word_count_dict[i] += num_entries
            """
            if i % 25 == 0:
                print(i)
            stuff = f.read()
            words = stuff.split()
            for word in words:
                if word[0].isalnum():
                    if word not in stopwords:
                        movie_hash.set_val(word, i)
        f.close()

    print(f"Total entries: {running_entries_count:,}")
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
