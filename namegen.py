from random import choice


# Define character classes such as "vowels" or "consonants"
# NOTE: Class names need to be single characters.
CLASSES = {
  "A": "aeiou",
  "K": "kst"
}

# Define patterns for given names, using the classes defined above
GIVEN_NAME_PATTERNS = [
  "KAAK",
  "KAKAK",
  "KAAKAK",
  "KAKAAK",
]

# Define patterns for surnames, using the classes defined above
SURNAME_PATTERNS = [
  "KAAK",
  "KAAKKA",
]


def generate_name(patterns, classes=CLASSES):
  pattern = choice(patterns)
  return ''.join(choice(classes[klass]) for klass in pattern).capitalize()


generate_given_name = lambda: generate_name(GIVEN_NAME_PATTERNS)
generate_surname = lambda: generate_name(GIVEN_NAME_PATTERNS)


def generate_full_name():
  given_name = generate_given_name()
  surname = generate_surname()
  return f"{given_name} {surname}"


if __name__ == "__main__":
  for i in range(10):
    print(generate_full_name())
