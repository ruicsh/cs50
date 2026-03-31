# import inflect


def main():
    # p = inflect.engine()

    names = get_names()
    # list = p.join(names)
    list = list_names(names)
    print(f"Adieu, adieu, to {list}")


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            return names


# instead of inflect.join
def list_names(names):
    if len(names) <= 2:
        return " and ".join(names)

    # # alternative with head/tail
    # head = ", ".join(names[:-1])
    # return f"{head}, and {names[len(names) - 1]}"

    # # alternative one-liner
    # return ", ".join(names)[::-1].replace(",", "dna ,", 1)[::-1]

    # join with comma, split at last comma, rejoin with ", and"
    lhs, _, rhs = ", ".join(names).rpartition(",")
    return lhs + ", and " + rhs


main()
