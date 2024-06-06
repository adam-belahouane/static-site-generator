import unittest
from markdowntohtml import markdown_to_blocks, markdown_to_html_node
from markdowntohtml import block_to_block_type, block_type_code, block_type_heading, block_type_ordered_list, block_type_paragraph, block_type_quote, block_type_unordered_list

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """.strip()

        expected_output = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        
        self.assertEqual(expected_output, markdown_to_blocks(markdown))
        print("All tests passed!")
    

class TestMarkdownBlockTypes(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_type_heading, block_to_block_type("# Heading 1"))
        self.assertEqual(block_type_heading, block_to_block_type("## Heading 2"))
        self.assertEqual(block_type_heading, block_to_block_type("### Heading 3"))
        self.assertEqual(block_type_heading, block_to_block_type("#### Heading 4"))
        self.assertEqual(block_type_heading, block_to_block_type("##### Heading 5"))
        self.assertEqual(block_type_heading, block_to_block_type("###### Heading 6"))

    def test_code_block(self):
        self.assertEqual(block_type_code, block_to_block_type("```\ncode block\n```"))
        self.assertEqual(block_type_code, block_to_block_type("```\nmultiple lines\nof code\n```"))

    def test_quote(self):
        self.assertEqual(block_type_quote, block_to_block_type("> This is a quote"))
        self.assertEqual(block_type_quote, block_to_block_type("> This is a quote\n> spanning multiple lines"))

    def test_unordered_list(self):
        self.assertEqual(block_type_unordered_list, block_to_block_type("* Item 1"))
        self.assertEqual(block_type_unordered_list, block_to_block_type("- Item 1\n- Item 2\n- Item 3"))
        self.assertEqual(block_type_unordered_list, block_to_block_type("* Item 1\n* Item 2\n* Item 3"))

    def test_ordered_list(self):
        self.assertEqual(block_type_ordered_list, block_to_block_type("1. First item"))
        self.assertEqual(block_type_ordered_list, block_to_block_type("1. First item\n2. Second item\n3. Third item"))

    def test_paragraph(self):
        self.assertEqual(block_type_paragraph, block_to_block_type("This is a normal paragraph."))
        self.assertEqual(block_type_paragraph, block_to_block_type("Another example of a paragraph\nwith multiple lines."))
    
    def test_paragraph_html(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

if __name__ == "__main__":
    unittest.main()


# Run the test
