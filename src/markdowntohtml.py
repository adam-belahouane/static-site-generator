from textnode import TextNode
import re
from htmlnode import LeafNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_list.append(TextNode(part, node.text_type))
                else:
                    new_list.append(TextNode(part, text_type))
        else:
            new_list.append(node)
    return new_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(
                TextNode(
                    image[0],
                    "image",
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, "text"))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, "text"))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    raw_blocks = [block.strip() for block in raw_blocks if block.strip()]

    raw_blocks = ['\n'.join(line.lstrip() for line in block.split('\n')) for block in raw_blocks]

    return raw_blocks

def block_to_block_type(block):
    if block.startswith("#"):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if all(line.startswith(">") for line in block.split("\n")):
        return block_type_quote
    if all(line.startswith(("* ", "- ")) for line in block.split("\n")):
        return block_type_unordered_list
    if all(line.startswith(f"{i}. ") for i, line in enumerate(block.split("\n"), 1)):
        return block_type_ordered_list
    return block_type_paragraph


