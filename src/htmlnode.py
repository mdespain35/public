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
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
        self.children = None

    def to_html(self):
        if  not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("tag is a required field")
        if not self.children:
            raise ValueError("no children detected")
        
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html

