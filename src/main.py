from textnode import TextNode, TextType

def main():
    foo = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(foo)


if __name__ == "__main__":
    main()