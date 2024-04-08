import unittest

from htmlnode import ParentNode
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_reqr(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])

    def test_to_html(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_parentNodeNesting(self):
        node = ParentNode("body",
        [
            ParentNode("main",[
                LeafNode("h1", "Main heading"),
                ParentNode("section", [
                    LeafNode("h2", "This is the Bold section"),
                    ParentNode("p", [
                        LeafNode(None, "This is a paragraph using the "),
                        LeafNode("b", "bold "),
                        LeafNode(None, "tag"),
                    ])
                ]),
                ParentNode("section", [
                    LeafNode("h2", "This is the italic section"),
                    ParentNode("p", [
                        LeafNode(None, "This is a paragraph using the "),
                        LeafNode("i", "italic "),
                        LeafNode(None, "tag"),
                    ]),
                ]),
                ParentNode("section", [
                    LeafNode("h2", "This is the Normal section"),
                    ParentNode("p", [
                        LeafNode(None, "This is a paragraph is normal but heres a "),
                        LeafNode("a", "link "),
                        LeafNode(None, "that does nothing"),
                    ])
                ])
            ])
        ])
        self.maxDiff = None
        self.assertEqual(node.to_html(), '<body><main><h1>Main heading</h1><section><h2>This is the Bold section</h2><p>This is a paragraph using the <b>bold </b>tag</p></section><section><h2>This is the italic section</h2><p>This is a paragraph using the <i>italic </i>tag</p></section><section><h2>This is the Normal section</h2><p>This is a paragraph is normal but heres a <a>link </a>that does nothing</p></section></main></body>')


if __name__ == "__main__":
    unittest.main()