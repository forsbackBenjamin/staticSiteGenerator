from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value!")
        if self.tag == None:
            return self.value
        if self.props != None:
            html_props = self.props_to_html()
        else:
            html_props = ""
        if self.tag != "img":
            return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
        return f"<{self.tag}{html_props} />"
        