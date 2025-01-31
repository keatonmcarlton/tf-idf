# hash table syntax borrowed from https://www.geeksforgeeks.org/hash-map-in-python/
# hash function adapted from https://gist.github.com/mengzhuo/180cd6be8ba9e2743753, utilizes
# djb2 made by Dan J Bernstein, using Meng Zhuo's syntax from github

# !/usr/bin/env python
# encoding: utf-8
import math

LOAD_FACTOR_LIMIT = 0.7


def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


# class for each individual word object in a script
class Word:

    def __init__(self, word, script, size):
        self.size = size
        self.script = [0] * size
        self.word = word
        self.increment_script(script)

    def set_word(self, string):
        self.word = string

    # if word is found in script, increment the script incident in the word object
    def increment_script(self, input_script):
        self.script[input_script] += 1

    # gets number of scripts that has word
    def get_total_scripts(self):
        count = 0
        for script in self.script:
            if script > 0:
                count += 1
        return count

    # idf = log(# of documents / # of documents that contain term)
    # using add one smoothing to avoid dividing by zero
    def idf(self):
        return math.log10(self.size / (self.get_total_scripts() + 1)) + 1

    # Used for testing. returns number of documents containing a term.
    def get_total_val(self):
        return sum(self.script)


class HashTable:
    def __init__(self, size, UBD):
        self.upper_bound_scripts = UBD
        self.size = size
        self.load_factor = LOAD_FACTOR_LIMIT
        self.hash_table = [[] for _ in range(self.size)]
        self.items = 0
        self.resized = 0

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # resizing hash function doubles the size and places them into new spots based on modulus of new size
    def resize(self):
        increased_size = self.size * 2
        table = [[] for _ in range(increased_size)]
        for bucket in self.hash_table:
            for word in bucket:
                index_new = hash_djb2(word.word) % increased_size
                table[index_new].append(word)
        self.size = increased_size
        self.hash_table = table
        self.resized += 1

    def checkLF(self):
        if self.items / self.size >= self.load_factor:
            self.resize()

    def set_val(self, input_word, script):
        # hash it
        post_hashed_key = hash_djb2(input_word) % self.size
        bucket = self.hash_table[post_hashed_key]
        # if bucket has word, increment word's script index
        for thing in bucket:
            if thing is None:
                break
            if thing.word == input_word:
                thing.increment_script(script)
                return

        # otherwise, make new word slot in the bucket
        bucket.append(Word(input_word, script, self.upper_bound_scripts))
        self.items += 1
        self.checkLF()

    # gets word object from string
    def get(self, input_word):
        bucket = self.hash_table[hash_djb2(input_word) % self.size]
        for thing in bucket:
            if thing.word == input_word:
                return thing
        return None

    # used only in testing, prints entire table
    def print_hash_table(self):
        for bucket in self.hash_table:
            for word in bucket:
                total_num = sum(word.script)
                print(f"({hash_djb2(word.word)}). {word.word}: {total_num}")

    # Used in testing. gets total use of a word throughout all scripts
    def get_total_val(self, input_word):
        # find bucket
        bucket = self.hash_table[hash_djb2(input_word) % self.size]

        # find word
        found = False
        for thing in bucket:
            if thing.word == input_word:
                found = True
                total_val = sum(thing.script)

        if found:
            return total_val
        else:
            return "No record found"
    # Used only in testing. gets total use of a word in given script
    def get_script_val(self, input_word, script):
        # find bucket
        bucket = self.hash_table[hash_djb2(input_word) % self.size]

        # find word
        found = False
        for thing in bucket:
            if thing.word == input_word:
                found = True
                val = thing.script[script]

        if found:
            return val
        else:
            return "No record found"
