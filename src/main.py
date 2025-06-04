import os, shutil
from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_to_html import markdown_to_html_node
def main():
    copy_static_to_public("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")

def copy_static_to_public(from_path, to_path):
    if not os.path.exists(from_path):
        raise Exception(f"{from_path} does not exist")
    if to_path == "public/" and os.path.exists(to_path):
        shutil.rmtree(to_path)
        os.mkdir("public")
    dir_items = os.listdir(from_path)
    for dir_item in dir_items:
        item_from_path = from_path + dir_item
        item_to_path = to_path + dir_item + "/"
        if os.path.isfile(item_from_path):
            shutil.copy(item_from_path, to_path)
        else:
            os.mkdir(item_to_path)
            copy_static_to_public(item_from_path + "/", item_to_path)
    
def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if len(line) > 2 and line[0:2] == "# ":
            return line[2:]
    raise Exception("No title was given in the markdown file")
            
def generate_page(from_path, template_path, dest_path):
    print(f"\nGenerating page from {from_path}, to {dest_path} using template {template_path}\n")
    with open(from_path) as markdown_path:
        markdown_file = markdown_path.read()
    with open(template_path) as template_path:
        template_file = template_path.read()
    html_string = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    template_file.replace("{{ Title }}", title)
    template_file.replace("{{ Content }}", html_string)
    open(dest_path, "x")
    with open(dest_path, "w") as dest_path:
        dest_path.write(template_file)

main()