import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestTextNode(unittest.TestCase):
    def test_prop1(self):
        node = HTMLNode("<p>", "Some text", [HTMLNode(), HTMLNode()], {"name": "Benjamin", "age": "27", "city": "Gothenburg"})
        props = node.props_to_html()
        self.assertEqual(props, ' name="Benjamin" age="27" city="Gothenburg"')

    def tesT_prop2(self):
        node = HTMLNode(props={"test": "test", "test2": "test2"})
        props = node.props_to_html()
        self.assertEqual(props, ' test="test" test2="test2"')
    
    def test_repr(self):
        node = HTMLNode("<h>")
        message = node.__repr__()
        self.assertEqual(message, "HTMLNode(tag=<h>,\n value=None,\n children=None,\n props=None)")
    
    def test_leaf_node(self):
        html_string = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(html_string, "<p>This is a paragraph of text.</p>")
    
    def test_leaf_node_prop(self):
        html_message = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(html_message, '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()