from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    foo = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    fooH = HTMLNode("a", "Testeburger", props={"href": "https://www.google.com",
    "target": "_blank",})
    print(foo)
    print(fooH)


if __name__ == "__main__":
    main()