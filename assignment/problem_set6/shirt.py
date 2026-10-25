from PIL import Image, ImageOps
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    if not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    input_ext = sys.argv[1].lower().split(".")[-1]
    output_ext = sys.argv[2].lower().split(".")[-1]

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as photo:
            shirt = Image.open("shirt.png")

            photo = ImageOps.fit(photo, shirt.size)
            photo.paste(shirt, mask=shirt)

            photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()