from textnode import *
from htmlnode import *

def main():
    foo = TextNode("This is a text node", TextType.TEXT)
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
    node2 = text_node_to_html_node(foo)
    #print(node.to_html())
    print(node2.to_html())
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


if __name__ == "__main__":
    main()