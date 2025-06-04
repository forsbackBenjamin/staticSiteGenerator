from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag!")
        if len(self.children) == 0 or self.children == None:
            raise ValueError("ParentNode must have children!")
        html_str = f"<{self.tag}>"
        for child in self.children:
            print(child)
            html_str = html_str + child.to_html()
        return html_str + f"</{self.tag}>"