# imports Natural Language Tool Kit popular package
import nltk
import os
import hash

nltk.download('popular')


def split(file_name):
    pieces = file_name.split('_', 2)
    return pieces[0], int(pieces[1])


def main():
    movie_hash = hash.HashTable
    directory = os.path.dirname(__file__)
    name_to_number_dictionary = {}
    number_to_name_dictionary = {}
    # this is the name of the folder that holds the text files of movie scripts
    file_folder = r"./raw_text_lemmas/"

    running_entries_count = 0
    for i, file_name in enumerate(os.listdir(file_folder)):
        # Open file
        with open(os.path.join(file_folder, file_name)) as f:
            name, num_entries = split(file_name)
            running_entries_count += num_entries
            name_to_number_dictionary[name] = i
            number_to_name_dictionary[i] = name
            print(f"{i}: '{name}'")

            #TODO: loop thru each file and increase each word occurence in script
            # ie: do movie_hash.set_val(word, script) -> this will increment if it exists and add it if it doesnt

    #TODO: tf-idf function

    print(f"Total entries: {running_entries_count:,}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
