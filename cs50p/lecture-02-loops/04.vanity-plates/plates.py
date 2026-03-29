def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        starts_with_two_letters(s)
        and has_required_length(s, 2, 6)
        and not has_numbers_in_middle(s)
        and not is_first_number(s, 0)
        and s.isalnum()
    )


# starts with two letters
def starts_with_two_letters(s):
    for c in s[0:2]:
        if not c.isalpha():
            return False

    return True


# check min and max length of str
def has_required_length(s, min, max):
    return min <= len(s) <= max


# check if there are numbers in the middle of str
def has_numbers_in_middle(s):
    digits = get_digits_chars()

    # remove all numbers from the end
    no_trailing_numbers = s.rstrip(digits)

    # if there are still numbers, there's numbers in the middle
    return find_first_of(no_trailing_numbers, digits) > -1


# check if the first digit found is the one given
def is_first_number(s, n):
    digits = get_digits_chars()
    index = find_first_of(s, digits)

    return s[index] == f"{n}"


# find first char of a list of chars in a string
def find_first_of(s, chars):
    first_char_index = len(s)
    for c in chars:
        index = s.find(c)
        if index > -1 and index < first_char_index:
            first_char_index = index

    return -1 if first_char_index == len(s) else first_char_index


# all of digits as str[]
def get_digits_chars():
    digits = ""
    for n in range(10):
        digits += f"{n}"
    return digits


main()
