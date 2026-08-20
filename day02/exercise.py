def calculate_area(length, width):
    return length * width


def calculate_perimeter(length, width):
    return length + width


def is_even(number):
    return number % 2 == 0


def get_largest(numbers):
    new = [0]
    for number in numbers:
        if number > new[0]:
            new[0] = number
    return new[0]


def count_vowels(text):
    count = 0
    for letter in text:
        if letter in ["a", "e", "i", "o", "u"]:
            count += 1
    return count
