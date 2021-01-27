from random import randint, choice

CLASSES = {
    "T": "dlkkkmnstttv",
    "A": "aaiooeu",
    "E": "aaiooeu",
}


def is_max_pred_reached(chars, pred, max_same):
    """
    Returns True if at least `max_same` characters from the end of `chars` match
    the predicate `pred`.

    >>> is_max_pred_reached("baa", lambda a: a == "a", 2)
    True
    >>> is_max_pred_reached("karva", lambda a: a in "aioeu", 2)
    False
    """
    found = 0

    for char in reversed(chars):
        if pred(char):
            found += 1
            if found >= max_same:
                return True
        else:
            return False

    return False


def is_max_same_class_reached(chars, klass, max_same_class):
    """
    >>> is_max_same_class_reached("baee", "ae", 3)
    True
    >>> is_max_same_class_reached("baee", "bt", 1)
    False
    """
    return is_max_pred_reached(chars, lambda c: c in klass, max_same_class)


def is_max_same_reached(chars, char, max_same):
    return is_max_pred_reached(chars, lambda c: c == char, max_same)


def generate_name(classes=CLASSES, min_length=4, max_length=10, max_same=2, max_same_class=3):
    chars = []

    for i in range(randint(min_length, max_length + 1)):
        if chars:
            valid_classes = [klass for klass in classes.values() if not is_max_same_class_reached(chars, klass, max_same_class)]
        else:
            valid_classes = list(classes.values())

        class_chars = choice(valid_classes)
        valid_chars = [char for char in class_chars if not is_max_same_reached(chars, char, max_same)]
        chars.append(choice(valid_chars))

    return ''.join(chars).capitalize()


def generate_full_name():
    given_name = generate_name()
    surname = generate_name()
    return f"{given_name} {surname}"


if __name__ == "__main__":
    for i in range(10):
        print(generate_full_name())
