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
        for k, v in self.props.items():
            html += f' {k}="{v}"'
        return html
    