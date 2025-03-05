import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="ul")
        self.assertEqual(f"{node}", "HTMLNode(ul, None, None)")

    def test_props(self):
        properties = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(tag="img", props=properties)
        self.assertEqual(f"{node}", 'HTMLNode(img, None, href="https://www.google.com" target="_blank")')
    def test_child(self):
        children= []
        children.append(HTMLNode(tag="p", value="A favorite book"))
        children.append(HTMLNode(value="The Rook"))
        properties = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        children.append(HTMLNode(tag="img", props=properties))
        node = HTMLNode("ul", children=children)
        expected ='''HTMLNode(ul, None, None)
* HTMLNode(p, A favorite book, None)
* HTMLNode(None, The Rook, None)
* HTMLNode(img, None, href="https://www.google.com" target="_blank")'''
        self.assertEqual(f"{node}", expected)

if __name__ == "__main__":
    unittest.main()