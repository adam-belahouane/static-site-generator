import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_reqr(self):
        node = LeafNode("p", "this is a test", {"href": "https://www.google.com", "target": "_blank"})

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()