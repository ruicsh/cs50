def main():
    coke_price = 50
    amount_due = coke_price

    while True:
        print("Amount Due: ", amount_due)
        coin = int(input("Insert Coin: "))
        amount_due -= coin
        if amount_due <= 0:
            print("Change Owed:", 0 - amount_due)
            break


main()
