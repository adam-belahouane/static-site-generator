from textnode import TextNode
import re
from htmlnode import LeafNode

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
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        li = node.text
        for match in matches:
            li = li.split(f"![{match[0]}]({match[1]})")
            new_nodes.append(TextNode(li[0], "text"))
            new_nodes.append(TextNode(match[0], "image", match[1]))
            del li[0]
            li = " ".join(li)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        li = node.text
        matches = extract_markdown_links(li)
        for match in matches:
            li = li.split(f"[{match[0]}]({match[1]})")
            new_nodes.append(TextNode(li[0], "text"))
            new_nodes.append(TextNode(match[0], "link", match[1]))
            del li[0]
            li = " ".join(li)
    return new_nodes

