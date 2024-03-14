class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, text):
        return self.text is text.text and self.text_type is text.text_type and self.url is text.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    