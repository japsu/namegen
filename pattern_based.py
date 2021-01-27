#!/usr/bin/env python3
from random import choice


# Define character classes such as "vowels" or "consonants"
# NOTE: Class names need to be single characters.
CLASSES = {
    "A": "aeiou",
    "T": "ntl",
    "K": "krsf",
    "N": "mn",
}

# Define patterns for given names, using the classes defined above
# The colon : can be used to denote double same character.
GIVEN_NAME_PATTERNS = [
    # Tuur
    "TA:K",
    # Nootka
    "TA:TKA",
    # Oofa
    "A:KA",
    # Ool
    "A:T",
    # Muust
    "NA:KT",
]

# Define patterns for surnames, using the classes defined above
SURNAME_PATTERNS = [
    # Soon
    "KA:N",
    # Sunt
    "KANT",
    # Kapik
    "KATAK",
    # Took
    "TA:K",
]


def generate_name(patterns, classes=CLASSES):
    pattern = choice(patterns)

    chars = []
    for klass in pattern:
        if klass == ":":
            chars.append(chars[-1])
        else:
            chars.append(choice(classes[klass]))

    return "".join(chars).capitalize()


generate_given_name = lambda: generate_name(GIVEN_NAME_PATTERNS)
generate_surname = lambda: generate_name(SURNAME_PATTERNS)


def generate_full_name():
    given_name = generate_given_name()
    surname = generate_surname()
    return f"{given_name} {surname}"


if __name__ == "__main__":
    for i in range(10):
        print(generate_full_name())
