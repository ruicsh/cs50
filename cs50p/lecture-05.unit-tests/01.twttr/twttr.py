def main():
    word = input("Input: ")
    output = shorten(word)
    print("Output:", output)


def shorten(word):
    output = word.lower()
    for vowel in "aeiou":
        output = output.replace(vowel, "")
    return output


if __name__ == "__main__":
    main()
