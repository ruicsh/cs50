import random


def main():
    level = get_int("Level: ")
    rand = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")
        if guess == rand:
            print("Just right!")
            break
        elif guess > rand:
            print("Too large!")
        else:
            print("Too small!")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
