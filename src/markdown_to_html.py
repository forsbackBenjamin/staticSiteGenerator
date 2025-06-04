from blocktype import markdown_to_blocks, block_to_block_type
from textnode import TextNode, TextType
from blocktype import BlockType
from leafnode import LeafNode
from parentnode import ParentNode
from split_nodes_with_delimiter import text_to_textnodes, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    blocks = list(map(lambda x: (x, block_to_block_type(x)), blocks))
    div_children = []
    for block in blocks:
        if block[1] == BlockType.HEADING:
            div_children.append(markdown_heading_to_html_node(block[0]))
        elif block[1] == BlockType.CODE:
            div_children.append(markdown_code_to_html_node(block[0]))
        elif block[1] == BlockType.QUOTE:
            div_children.append(markdown_quote_to_html_node(block[0]))
        elif block[1] == BlockType.UNORDERED_LIST:
            div_children.append(markdown_list_to_html_nodes(block[0], False))
        elif block[1] == BlockType.ORDERED_LIST:
            div_children.append(markdown_list_to_html_nodes(block[0], True))
        elif block[1] == BlockType.PARAGRAPH:
            text_node = paragraph_block_to_text_node(block[0])
            if text_node.text_type == TextType.TEXT:
                text_node_children = text_to_textnodes(text_node.text)
                if len(text_node_children) == 1:
                    div_children.append(text_node_to_html_node(text_node_children))
                else:
                    leaf_nodes = list(map(lambda x: text_node_to_html_node(x), text_node_children))
                    div_children.append(ParentNode("p", leaf_nodes))                    
            else:
                div_children.append(text_node)
    return ParentNode("div", div_children)



    
def markdown_heading_to_html_node(markdown_heading):
    heading_level = len(markdown_heading) - len(markdown_heading.lstrip('#'))
    tag = f"h{heading_level}"
    return LeafNode(tag, markdown_heading[heading_level:])

def markdown_code_to_html_node(markdown_code):
    markdown_code = markdown_code.strip("`")
    #markdown_code = markdown_code.strip()
    markdown_code = markdown_code.lstrip("\n")
    tag = "code"
    leaf = LeafNode(tag, markdown_code)
    return ParentNode("pre", [leaf])

def markdown_quote_to_html_node(markdown_quote):
    markdown_quote = markdown_quote[1:].strip()
    tag = "blockquote"
    return LeafNode(tag, markdown_quote)

def markdown_list_to_html_nodes(markdown_list, ordered):
    items = markdown_list.split("\n")
    list_children = []
    if not ordered:
        for item in items:
            list_children.append(LeafNode("li", item[1:].strip()))
    if ordered:
        for item in items:
            list_children.append(LeafNode("li", item[2:].strip()))
    if ordered:
        list_node = ParentNode("ol", list_children)
    else:
        list_node = ParentNode("ul", list_children)
    return list_node



def paragraph_block_to_text_node(text_block):
    text_block = text_block.replace("\n", " ")
    if len(text_block) >= 4 and text_block[0:3] == "**" and text_block[-2:] == "**":
        return TextNode(text_block[2:-2], TextType.BOLD)
    elif len(text_block) >= 2 and text_block[0] == "_" and text_block[-1] == "_":
        return TextNode(text_block[1:-1], TextType.ITALIC)
    return TextNode(text_block, TextType.TEXT)
    

def text_to_children(text):
    raise NotImplementedError()