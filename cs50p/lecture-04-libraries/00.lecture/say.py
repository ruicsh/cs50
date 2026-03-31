import sys

import cowsay

from sayings import hello, goodbye


if len(sys.argv) != 2:
    sys.exit()

cowsay.cow(f"hello, {sys.argv[1]}")

hello(sys.argv[1])
goodbye(sys.argv[1])
