# Project 3 - Movie Recommendations with TF-IDF

---
Don't know what to watch? 
This project allows users to enter a word, and returns five movie recommendations that match that word. 
This is based on the **term frequency - inverse document frequency (tf-idf)** of the word in each movie's script.

>"The first is the **term frequency**: the frequency of the word t in the
document *d*... The [**inverse document frequency**] is used to give a higher weight to words that occur
only in a few documents...The tf-idf weighting is the way for weighting co-occurrence matrices in information retrieval." (Jurafsky, D. & Martin, J.H. (2024). *Speech and Language Processing (3rd ed. draft)*)

## Getting Started

---
The main functionality exists in the `main.py` file. 
To begin, run the program, and wait for the documents 
to be completely loaded into the data structure for retrieval. 

You will then be prompted to enter a word. This word will be lemmatized 
for easier searching and space preservation. For example, the words:
- run
- runs
- running
- ran

Would all be lemmatized to **run**. 

The program will then search the unordered map (backed here by 
a hash table) and return a list of five movies for you to watch. 

## Program running slowly?

---

It is normal for the first search to take a little longer load than subsequent searches. 

Our corpus of movie scripts is fairly large, with the
2,557 possible movies recommendations having thousands of unique words in their scripts. 
When accessing all 2,557 movies, it is possible for the program to take
around four minutes to load. If you would like the pool of possible
movie recommendations to be smaller (and for the program to load faster), 
you will need to change one number in the `main.py` file. 

In `main.py`, `line 46`:

`for x in range(1, 9):`

This line controls which `data/movie scripts {x}.zip` files will be scanned by 
the program. If you would only like to see recommendations from specific zip files,
you will need to change the range. See the examples below:

- for accessing the first four zip files: `for x in range(1, 5):`
- for accessing the last four zip files: `for x in range(4, 9):`
- for accessing `movie scripts 5.zip` only: `for x in range(5, 6)`