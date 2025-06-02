from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if block == "":
            blocks.remove(block)
    return block

def block_to_block_type(block):
    if block[0] == "#":
        if len(block) > 6 and block[0:6] != "#######":
            return BlockType.HEADING
        elif len(block) <= 6:
            return BlockType.HEADING
    elif block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    block_lines = block.split("\n")
    is_quote = True
    is_u_list = True
    is_o_list = True
    for line in block_lines:
        if line[0] != ">":
            is_quote = False
        if line[0] != "-":
            is_u_list = False
        if line[0] != ".":
            is_o_list = False
    if is_quote:
        return BlockType.QUOTE
    if is_u_list:
        return BlockType.UNORDERED_LIST
    if is_o_list:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH