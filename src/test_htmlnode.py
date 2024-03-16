import unittest

from htmlnode import HTMLNode

# unittest only runs a test if the file starts with test

class TestHTMLNode(unittest.TestCase):
    def test_reqr(self):
        node = HTMLNode("p", "this is a test", None, {"href": "https://www.google.com", "target": "_blank"})
        print(repr(node))
    
    def test_props_to_html(self):
        node = HTMLNode("p", "this is a test", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()