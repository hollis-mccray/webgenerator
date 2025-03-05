from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag not defined")
        if not self.children:
            raise ValueError("children not defined")

        child_text = ""
        for child in self.children:
            child_text += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_text}</{self.tag}>"