# imports Natural Language Tool Kit popular package
import nltk
import os
nltk.download('popular')
def main():
    # this is the name of the folder that holds the text files of movie scripts
    file_folder = r"C:\Users\Lily\Downloads\raw_text_lemmas\raw_text_lemmas"
    for name in os.listdir(file_folder):
        # Open file
        with open(os.path.join(file_folder, name)) as f:
            print(f"Content of '{name}'")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
