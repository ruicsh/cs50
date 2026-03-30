def main():
    items = get_items()
    list = make_list(items)
    print_list(list)


# build a list of items by asking the user, item by item
def get_items():
    items = []
    while True:
        try:
            item = input()
            items.append(item)
        except EOFError:
            print("")
            return items


# from a list of items, group and count them
def make_list(items):
    my_list = {}
    for item in items:
        if item not in my_list:
            my_list[item] = 1
        else:
            my_list[item] += 1

    return dict(sorted(my_list.items()))


# print count and uppercased item
def print_list(list):
    for item in list:
        print(list[item], item.upper())


main()
