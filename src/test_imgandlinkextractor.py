import unittest

from markdowntohtml import extract_markdown_images
from markdowntohtml import extract_markdown_links
from markdowntohtml import split_nodes_image, split_nodes_link, text_to_textnodes
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
    
    def test_text_to_textnode(self):
        result = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)")
        test_case = [
                    TextNode("This is ", "text"),
                    TextNode("text", "bold"),
                    TextNode(" with an ", "text"),
                    TextNode("italic", "italic"),
                    TextNode(" word and a ", "text"),
                    TextNode("code block", "code"),
                    TextNode(" and an ", "text"),
                    TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                    TextNode(" and a ", "text"),
                    TextNode("link", "link", "https://boot.dev"),
                ]
        self.assertEqual(result, test_case)


    

if __name__ == "__main__":
    unittest.main()