# youtuber = input("What's your favourite youtuber? ")  # some string variable
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adjective:")
verb1 = input("verb:")
verb2 = input("verb:")
person = input("person:")
madlib = f"python is so {adj}! It makes me so excited because I like to {verb1}.keep persevering and {verb2} " \
         f"like you are {person}!"
print(madlib)

import random


def get_word(type):
    if type == 'noun':
        return input("Enter a noun: ")
    elif type == 'verb':
        return input("Enter a verb: ")
    elif type == 'adjective':
        return input("Enter an adjective: ")
    elif type == 'adverb':
        return input("Enter an adverb: ")
    else:
        return ""


def generate_madlib():
    story = f"Once upon a time, there was a {get_word('adjective')} {get_word('noun')} who loved to {get_word('verb')} {get_word('adverb')}."
    story += f" One day, they found a {get_word('noun')} and decided to {get_word('verb')} it {get_word('adverb')}."
    story += f" This made them feel very {get_word('adjective')} and they lived happily ever after."

    print("\nYour Madlib Story:\n")
    print(story)


if __name__ == "__main__":
    print("Welcome to the Advanced Madlib Game!")
    generate_madlib()

import random


def get_word(type):
    if type == 'noun':
        return input("Enter a noun: ")
    elif type == 'verb':
        return input("Enter a verb: ")
    elif type == 'adjective':
        return input("Enter an adjective: ")
    elif type == 'adverb':
        return input("Enter an adverb: ")
    elif type == 'plural_noun':
        return input("Enter a plural noun: ")
    elif type == 'place':
        return input("Enter a place: ")
    else:
        return ""


def generate_madlib():
    story = f"In a {get_word('adjective')} {get_word('place')}, there were {get_word('plural_noun')} who loved to {get_word('verb')} {get_word('adverb')}."
    story += f" Every {get_word('noun')} would {get_word('verb')} around the {get_word('place')}, looking for {get_word('adjective')} {get_word('plural_noun')}."
    story += f" One day, they discovered a {get_word('noun')} that could {get_word('verb')} {get_word('adverb')} and decided to {get_word('verb')} it {get_word('adverb')}."

    print("\nYour Madlib Story:\n")
    print(story)


if __name__ == "__main__":
    print("Welcome to the Advanced Madlib Game!")
    generate_madlib()
