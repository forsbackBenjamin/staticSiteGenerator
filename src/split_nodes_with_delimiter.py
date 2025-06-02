import re
from textnode import TextNode, TextType
from leafnode import LeafNode

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_node = node.text.split(delimeter)
        if len(split_node) % 2 != 1:
            raise Exception("No matching closing {delimeter}, invalid markdown syntax")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            for i, segment in enumerate(split_node):
                if i%2==0:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(segment, text_type))
    return new_nodes

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
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextNode does not have a proper HTML type causing conversion error.")


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue
        for image in images:
            node_text = text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if node_text[0] != "":
                new_nodes.append(TextNode(node_text[0], node.text_type))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if len(node_text) == 2:
                text = node_text[1]       
        if len(node_text) == 2 and node_text[1] != "":
            new_nodes.append(TextNode(node_text[1], node.text_type))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        for link in links:
            node_text = text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            if node_text[0] != "":
                new_nodes.append(TextNode(node_text[0], node.text_type))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if len(node_text) == 2:
                text = node_text[1]       
        if len(node_text) == 2 and node_text[1] != "":
            new_nodes.append(TextNode(node_text[1], node.text_type))
    return new_nodes

def text_to_textnodes(text):
    nodes = []
    starting_node = TextNode(text, TextType.TEXT)
    nodes.append(starting_node)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n").strip()
    for block in blocks:
        if block == "":
            blocks.remove(block)
    return block
    