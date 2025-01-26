import unittest

from htmlnode import HTMLNode

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