expression = input("Expression: ")

x, y, z = expression.split(" ")
x = float(x)
z = float(z)


match y:
    case "+":
        value = x + z
    case "-":
        value = x - z
    case "*":
        value = x * z
    case "/":
        value = x / z
    case _:
        value = -1


print(f"{value:.1f}")
