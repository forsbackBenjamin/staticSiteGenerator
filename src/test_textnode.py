import unittest

from textnode import TextNode, TextType

from main import text_node_to_html_node
from split_nodes_with_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://amazon.com")
        self.assertNotEqual(node, node2)
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)
    def test_not_eq_text(self):
        node = TextNode("This", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)
    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_split_text_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, answer)
    def test_split_text_node2(self):
        node = TextNode("This is text with _a __code block word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        answer = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("a ", TextType.ITALIC),
            TextNode("", TextType.TEXT),
            TextNode("code block word", TextType.ITALIC),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, answer)
    def test_split_text_node2(self):
        node = TextNode("This is text with **a ****code block word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        answer = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("a ", TextType.BOLD),
            TextNode("", TextType.TEXT),
            TextNode("code block word", TextType.BOLD),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, answer)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
if __name__ == "__main__":
    unittest.main()