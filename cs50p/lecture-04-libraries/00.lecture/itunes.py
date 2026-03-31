import sys

import requests


if len(sys.argv) != 2:
    sys.exit()


url = "https://itunes.apple.com/search?entity=song&term=" + sys.argv[1]
response = requests.get(url)
o = response.json()

for result in o["results"]:
    print(result["trackName"])
