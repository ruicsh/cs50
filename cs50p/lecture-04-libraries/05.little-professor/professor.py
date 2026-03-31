import random


def main():
    level = get_level()

    problems = []
    for _ in range(10):
        problem = generate_problem(level)
        problems.append(problem)

    score = 0
    for problem in problems:
        score += solve_problem(problem)

    print(f"Score: {score}")


# ask user for solution for a problem
def solve_problem(problem):
    tries = 3
    x, y, solution = problem
    while True:
        try:
            if tries == 0:
                print(f"Solution: {solution}")
                return 0

            guess = int(input(f"{x} + {y} = "))
            if guess != solution:
                tries -= 1
                raise ValueError

            return 1

        except ValueError:
            print("EEE")


# get number of digits, possible: 1, 2, or 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


# generate problem with level
def generate_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    sum = x + y

    return [x, y, sum]


# generate an integer with n digits
def generate_integer(n_digits):
    number = ""
    for _ in range(n_digits):
        number += f"{random.randint(0, 9)}"

    return int(number)


if __name__ == "__main__":
    main()
