import unittest
from generate_page import *

class TestPageGenerator(unittest.TestCase):
    def test_find_title(self):
        md="""
# My Favorite RPGS

- [Star Trek Adventures](https://modiphius.us)
- [City of Mist/:Otherscape/Legend in the Mist](https://cityofmist.co)

# Fuck these guys:

- [Dungeons & Dragons](https://www.dndbeyond.com)
- [Palladium Books](https://palladiumbooks.com)
"""
        title = extract_title(md)
        self.assertEqual(title,"My Favorite RPGS")

    def test_no_title(self):
        md="""
My Favorite RPGS

- [Star Trek Adventures](https://modiphius.us)
- [City of Mist/:Otherscape/Legend in the Mist](https://cityofmist.co)

Fuck these guys:

- [Dungeons & Dragons](https://www.dndbeyond.com)
- [Palladium Books](https://palladiumbooks.com)
"""
        self.assertRaises(Exception,extract_title,markdown="md")