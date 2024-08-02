import hash
import numpy as np


def main():
    number_of_scripts = 15
    myhash = hash.HashTable(number_of_scripts)
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
            print(f"Hash value for this word: {myhash.get_possible_hash_value(WORD)}")
            print(f"This script count of this word: {myhash.get_script_val(WORD, SCRIPT)}")
            print(f"Total count of this word: {myhash.get_total_val(WORD)}")
            print(f"Current Load Factor: {myhash.items / myhash.size}")
            print()
    myhash.print_hash_table()

if __name__ == '__main__':
    main()
