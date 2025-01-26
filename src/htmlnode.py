class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):

        return f"HTMLNode:\nTag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}\n"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ''
        if self.props:
            for k, v in self.props.items():
                html += f' {k}="{v}"'
        return html

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.children = None

    def to_html(self):
        if len(self.value) == 0:
            raise ValueError
        if len(self.tag) == 0:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'