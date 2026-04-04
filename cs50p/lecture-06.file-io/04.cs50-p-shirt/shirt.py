import sys

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    filename_in = sys.argv[1]
    filename_out = sys.argv[2]

    shirt = Image.open("shirt.png")

    with Image.open(filename_in) as image:
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, mask=shirt)
        image.save(filename_out)


main()
