import re
from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextNode does not have a proper HTML type causing conversion error.")
                

def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    output = list(map(lambda x: (x.split("(")[0], x.split("["), matches)))
    return output

main()