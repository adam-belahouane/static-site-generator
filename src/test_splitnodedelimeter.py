import unittest
from markdowntohtml import split_nodes_delimiter
from textnode import TextNode

unittest.util._MAX_LENGTH=2000

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_Case1(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.maxDiff = None
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
            ])

if __name__ == "__main__":
    unittest.main()