import unittest
from textnode import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    markdown_to_blocks,
    block_to_block_type,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])


class TestExtractMarkdownImages(unittest.TestCase):
    def test_empty_text(self):
        imgs = extract_markdown_images("")
        self.assertListEqual(imgs, [])

    def test_no_images(self):
        imgs = extract_markdown_images("there are no images here gandalf")
        self.assertListEqual(imgs, [])

    def test_incorrect_image_markdown(self):
        imgs = extract_markdown_images("[nope](https://i.imgur.com/aKaOqIh.gif)")
        self.assertListEqual(imgs, [])

    def test_correct_image_markdown(self):
        imgs = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)")
        self.assertListEqual(imgs, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_correct_multiple_image_markdown(self):
        imgs = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertListEqual(imgs, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_empty_text(self):
        lnks = extract_markdown_links("")
        self.assertListEqual(lnks, [])

    def test_no_links(self):
        lnks = extract_markdown_links("there are no links here gandalf")
        self.assertListEqual(lnks, [])

    def test_incorrect_link_markdown(self):
        lnks = extract_markdown_links("![nope](https://i.imgur.com/aKaOqIh.gif)")
        self.assertListEqual(lnks, [])

    def test_correct_link_markdown(self):
        lnks = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual(lnks, [("to boot dev", "https://www.boot.dev")])

    def test_correct_multiple_links_markdown(self):
        lnks = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual(lnks, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        result = [
            '# This is a heading', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block', 
            '* This is a list item', '* This is another list item'
            ]
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        self.assertListEqual(result, markdown_to_blocks(markdown))
    
    def test_remove_whitespace(self):
        markdown = "      test      "
        self.assertListEqual(["test"], markdown_to_blocks(markdown))

    def test_empty_block(self):
        self.assertEqual("paragraph", block_to_block_type(""))
    
    def test_heading_block(self):
        self.assertEqual("heading", block_to_block_type("# test heading"))
    
    def test_too_many_hashmarks(self):
        self.assertEqual("paragraph", block_to_block_type("####### Master Skywalker there's too many of them!"))
    
    def test_coding_block(self):
        self.assertEqual("code", block_to_block_type("```\ncode block test\n```"))

    def test_incorrect_code_block(self):
        self.assertEqual("paragraph", block_to_block_type("```where are those backtickas?"))

    def test_quote_block(self):
        self.assertEqual("quote", block_to_block_type(">What a cool quote!"))

    def test_ul_asterisk(self):
        self.assertEqual("unordered_list", block_to_block_type("* Wow it works!"))

    def test_ul_dash(self):
        self.assertEqual("unordered_list", block_to_block_type("- Wow it works!"))
    
    def test_ul_no_space(self):
        self.assertEqual("paragraph", block_to_block_type("*Oh no, there is no space!"))

    def test_ol_block(self):
        self.assertEqual("ordered_list", block_to_block_type("1. The beginning"))
    
    def test_ol_no_space(self):
        self.assertEqual("paragraph", block_to_block_type("1.This is incorrect"))

if __name__ == "__main__":
    unittest.main()
