def main():
    word = input("Input: ")
    output = word
    for vowel in "aeiou":
        output = output.replace(vowel, "")
    print("Output:", output)


main()
