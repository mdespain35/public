from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    foo = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    fooH = HTMLNode("a", "Testeburger", props={"href": "https://www.google.com",
    "target": "_blank",})
    print(foo)
    print(fooH)
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    print(node.to_html())


if __name__ == "__main__":
    main()