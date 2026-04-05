def total(galleons: int, sickles: int, knuts: int) -> int:
    return (galleons * 17 + sickles) * 29 + knuts


def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


def my_print(*objects, sep=" ", end="\n"):
    s = ""
    for object in objects:
        s += object + sep
    print(s.rstrip(sep))


coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts")


f(100, 50, 25, galleons=100, sickels=50, knuts=25)
my_print("foo", "bar", sep="_")
