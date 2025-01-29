from textnode import *
from htmlnode import *

def main():
    text = "      test     "
    blocks = markdown_to_blocks(text)
    print(blocks)


if __name__ == "__main__":
    main()