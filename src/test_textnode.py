import unittest

from textnode import TextNode

# unittest only runs a test if the file starts with test

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a different text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_url_is_none(self):
        node = TextNode("test", "test_type")
        self.assertIsNone(node.url)
    
    def test_texttype_not_eq(self):
        node = TextNode("This is a different text node", "bold")
        node2 = TextNode("This is a text node", "normal")
        self.assertNotEqual(node.text_type, node2.text_type)


if __name__ == "__main__":
    unittest.main()
