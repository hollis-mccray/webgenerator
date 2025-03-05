import unittest

from textnode import *
from inline_markdown import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("City of Mist", TextType.LINK, url="https://cityofmist.co/")
        node2 = TextNode("City of Mist", TextType.LINK, url="https://cityofmist.co/")
        self.assertEqual(node, node2)

    def test_url_neq(self):
        node = TextNode("City of Mist", TextType.LINK, url="https://cityofmist.co/")
        node2 = TextNode("City of Mist", TextType.CODE, url="https://cityofmist.co/")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold text node</b>")

    def test_text_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is an italic text node</i>")

    def test_text_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a code text node</code>")

    def test_text_link(self):
        node = TextNode("City of Mist", TextType.LINK,  url="https://cityofmist.co/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://cityofmist.co/">City of Mist</a>')

    def test_text_image(self):
        node = TextNode("Kitsune", TextType.IMAGE, url="https://cityofmist.co/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="https://cityofmist.co/" alt="Kitsune"> </img>')


if __name__ == "__main__":
    unittest.main()