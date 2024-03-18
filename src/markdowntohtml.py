from textnode import TextNode

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