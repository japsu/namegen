#!/usr/bin/env python3
from random import choice, randint

VOWELS = "aaiooeu"
CONSONANTS = "bkkknsttv"


def generate_name(min_vowels=3, max_vowels=5, min_consonants=2, max_consonants=6):
    # Start by picking vowels
    chars = [choice(VOWELS) for i in range(randint(min_vowels, max_vowels + 1))]

    # Then sprinkle consonants
    consonant_indices = {choice(range(len(chars) + 1)) for i in range(randint(min_consonants, max_consonants + 1))}
    for index, offset in enumerate(consonant_indices):
        chars.insert(index + offset, choice(CONSONANTS))

    return ''.join(chars).capitalize()


def generate_full_name():
    given_name = generate_name()
    surname = generate_name()
    return f"{given_name} {surname}"


if __name__ == "__main__":
    for i in range(10):
        print(generate_full_name())
