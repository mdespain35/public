import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html = HTMLNode(props={"href": "https://www.google.com",
    "target": "_blank",})
        check_str = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html.props_to_html(), check_str)

    def test_empty_html_node(self):
        html = HTMLNode()
        self.assertIsNone(html.tag)
        self.assertIsNone(html.value)
        self.assertIsNone(html.children)
        self.assertIsNone(html.props)
    
    def test_no_children(self):
        html = HTMLNode("a", "Click Here!", props={"class": "test"})
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Click Here!")
        self.assertIsNone(html.children)
        self.assertEqual(html.props, {"class": "test"})

class TestLeafNode(unittest.TestCase):
    def test_empty_leaf_node(self):
        leaf = LeafNode('', '')
        with self.assertRaises(ValueError):
            leaf.to_html()
    
    def test_to_html(self):
        leaf1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(leaf2.to_html(), '<p>This is a paragraph of text.</p>')
    
    def test_empty_tag(self):
        leaf = LeafNode("", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "This is a paragraph of text.")

class TestParentNode(unittest.TestCase):
    def test_empty_parent(self):
        node = ParentNode('', [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_tag(self):
        node = ParentNode('', [LeafNode("b", "Bold text")])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_empty_children(self):
        node = ParentNode('a', [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_in_parent(self):
        compare = '<p><p><b>Bold text</b></p></p>'
        node = ParentNode("p", [ParentNode("p", [LeafNode("b", "Bold text"),]),],)
        self.assertEqual(node.to_html(), compare)

    def test_multiple_children(self):
        compare = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
        self.assertEqual(node.to_html(), compare)