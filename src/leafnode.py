from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value")
        if self.tag == None:
            return self.value
        if self.props != None:
            html_props = self.props_to_html
            print(f"\n\n\n {html_props}\n\n\n")
        else:
            html_props = ""
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"