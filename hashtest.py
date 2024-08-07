from nltk import WordNetLemmatizer

import hash
import numpy as np


def main():
    words = 5
    myhash = hash.HashTable(words, 20)
    guy = True
    while guy:
        WORD = input("Enter word (use '0' to exit): ")
        if WORD == "0":
            guy = False
            break
        else:
            SCRIPT = int(input("Enter script (use positive integer): "))
            myhash.set_val(WORD, SCRIPT)
            print()
            lem = WordNetLemmatizer()
            newword = lem.lemmatize(WORD)
            print(f"Word lemmatized: {newword}")
            print(f"This script count of this word: {myhash.get_script_val(WORD, SCRIPT)}")
            print(f"Total count of this word: {myhash.get_total_val(WORD)}")
            print(f"Current Load Factor: {myhash.items / myhash.size}")
            print(f"Resized Count: {myhash.resized}")
            print()
    myhash.print_hash_table()

if __name__ == '__main__':
    main()
