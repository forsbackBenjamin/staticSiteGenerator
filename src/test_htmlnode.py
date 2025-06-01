import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_prop1(self):
        node = HTMLNode("<p>", "Some text", [HTMLNode(), HTMLNode()], {"name": "Benjamin", "age": "27", "city": "Gothenburg"})
        props = node.props_to_html()
        self.assertEqual(props, " name=Benjamin age=27 city=Gothenburg")

    def tesT_prop2(self):
        node = HTMLNode(props={"test": "test", "test2": "test2"})
        props = node.props_to_html()
        self.assertEqual(props, " test=test test2=test2")
    
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

if __name__ == "__main__":
    unittest.main()