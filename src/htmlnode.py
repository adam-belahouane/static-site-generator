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
        for prop in self.props:
            html = html + " " + prop + f'="{self.props[prop]}"'
    
        return html



