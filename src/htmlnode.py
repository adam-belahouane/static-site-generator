class HTMLNode:

    def __init__(self, tag = None, value = None, children =None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return F"{self.tag}, {self.value}, {self.children}, {self.props}"

    def to_html(self):
        raise NotImplementedError("not put in place")

    def props_to_html(self):
        html = ''
        if not self.props:
            return html
        for prop in self.props:
            html = html + " " + prop + f'="{self.props[prop]}"'
    
        return html



class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        if value is None:
            raise ValueError("Value cannot be None for LeafNode")
        super().__init__(tag, value, None, props)

    def to_html(self):
        html = ""
        if self.tag:
            html += f"<{self.tag}{self.props_to_html()}>"
        html += self.value
        if self.tag:
            html += f"</{self.tag}>"
        return html



class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None):
        if not tag:
            raise ValueError("No Tag providied")
        if not children:
            raise ValueError("No kids")
        super().__init__(tag, None, children, None)
    
    def to_html(self):
        html = f"<{self.tag}>"
        for child in self.children:
            html = html + child.to_html()
        html += f"</{self.tag}>"
        return html

def text_node_to_html_node(text_node):
    tag, value, props = 0, None, None
    if text_node.text:
        value = text_node.text
    if text_node.text_type == "text":
        tag = None
    if text_node.text_type == "bold":
        tag = "b"
    if text_node.text_type == "italic":
        tag = "i"
    if text_node.text_type == "code":
        tag = "code"
    if text_node.text_type == "link":
        tag = "a"
        props = {"href" : f"{text_node.url}"}
    if text_node.text_type == "image":
        tag = "img"
        props =  {"src" : f"{text_node.url}", "alt" : "this is a img"}
    if tag == 0:
        raise Exception("invalid tag")
    
    return LeafNode(tag, value, props)        