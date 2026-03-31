import sys

import requests


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        url = "https://api.coinbase.com/v2/prices/BTC-USD/buy"
        response = requests.get(url)
        o = response.json()
        price = float(o["data"]["amount"])

        print(f"${price * n:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")


main()
