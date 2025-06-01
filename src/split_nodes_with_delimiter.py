from textnode import TextNode, TextType

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
        