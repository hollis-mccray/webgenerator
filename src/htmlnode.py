class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        child_text = ""
        if self.children:
            for child in self.children:
                child_text += f"\n* {child}"
        props = self.props_to_html()
        if len(props) != 0:
            return f"({self.tag}, {self.value},{self.props_to_html()}){child_text}"
        else:
            return f"HTMLNode({self.tag}, {self.value}, None){child_text}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        prop_string = ""
        for property in self.props:
            prop_string += f" {property}=\"{self.props[property]}\""
        return prop_string

