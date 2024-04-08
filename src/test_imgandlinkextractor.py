import unittest

from markdowntohtml import extract_markdown_images
from markdowntohtml import extract_markdown_links
from markdowntohtml import split_nodes_image, split_nodes_link
from textnode import TextNode

class TestImgandLinkFunctions(unittest.TestCase):
    def test_imgfunc(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_linkfunc(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        result = extract_markdown_links(text)
        self.assertEqual(result,[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_imgSplit(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        "text")
        result = split_nodes_image([node])
        nodelist = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", "text"),
            TextNode(
                "second image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
                    ]

        self.assertEqual(result, nodelist)
    
    def test_linkSplit(self):
        node = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", "text")
        result = split_nodes_link([node])
        nodelist = [
            TextNode("This is text with a ", "text"),
            TextNode("link", "link", "https://www.example.com"),
            TextNode(" and ", "text"),
            TextNode(
                "another", "link", "https://www.example.com/another"
            ),
                    ]
        self.assertEqual(result, nodelist)

    

if __name__ == "__main__":
    unittest.main()