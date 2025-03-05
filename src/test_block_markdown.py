import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocks_with_links(self):
        md="""
Right now these are my favorite RPGS:

- [Star Trek Adventures](https://modiphius.us)
- [City of Mist/:Otherscape/Legend in the Mist](https://cityofmist.co)

Fuck these guys:

- [Dungeons & Dragons](https://www.dndbeyond.com)
- [Palladium Books](https://palladiumbooks.com)
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Right now these are my favorite RPGS:",
                "- [Star Trek Adventures](https://modiphius.us)\n- [City of Mist/:Otherscape/Legend in the Mist](https://cityofmist.co)",
                "Fuck these guys:",
                "- [Dungeons & Dragons](https://www.dndbeyond.com)\n- [Palladium Books](https://palladiumbooks.com)"

            ],
        )

    def test_blocks_headers(self):
        blocks = [
            "# Header 1",
            "## Header 2",
            "### Header 3",
            "#### Header 4"
            "##### Header 5",
            "###### Header 6",
        ]

        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        self.assertNotEqual(block_to_block_type("######## Header 8, but that doesn't exist"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("######## Header 8, but that doesn't exist"), BlockType.PARAGRAPH)

    def test_blocks_code(self):
        yes = """```
Code all the things!
```"""
        crash = """```
Code all the things!
"""
        self.assertEqual(block_to_block_type(yes), BlockType.CODE)
        self.assertNotEqual(block_to_block_type(crash), BlockType.CODE)
        self.assertEqual(block_to_block_type(crash), BlockType.PARAGRAPH)

    def test_blocks_quote(self):

        succeed = """>Start where you are.
>Use what you have.
>Do what you can."""
        fail=""">Start where you are.
Use what you have.
>Do what you can."""
        self.assertEqual(block_to_block_type(succeed), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type(fail), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(fail), BlockType.PARAGRAPH)

    def test_blocks_ul(self):

        succeed = """- Alpha Quadrant
- Beta Quadrant
- Delta Quadrant
- Gamma Quadrant"""
        fail="""- Alpha Quadrant
- Beta Quadrant
- Delta Quadrant
Gamma Quadrant"""
        self.assertEqual(block_to_block_type(succeed), BlockType.UNORDERED_LIST)
        self.assertNotEqual(block_to_block_type(fail), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(fail), BlockType.PARAGRAPH)

    def test_blocks_ol(self):

        succeed = """1. Star Trek: The Motion Picture
2. Star Trek II: The Wrath of Khan
3. Star Trek III: The Search for Spock
4. Star Trek IV: The Voyage Home"""
        fail="""1. Star Trek: The Motion Picture
2. Star Trek II: The Wrath of Khan
3, Star Trek III: The Search for Spock
4. Star Trek IV: The Voyage Home"""
        self.assertEqual(block_to_block_type(succeed), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type(fail), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(fail), BlockType.PARAGRAPH)