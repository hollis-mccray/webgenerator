from textnode import *
from block_markdown import *
from inline_markdown import text_to_text_nodes
from parentnode import *

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for md_block in markdown_blocks:
        new_nodes  = []
        block_type = block_to_block_type(md_block)
        if block_type == BlockType.HEADING:
            new_nodes  = node_heading(md_block)
        elif block_type == BlockType.CODE:
            new_nodes  = node_code(md_block)
        elif block_type == BlockType.QUOTE:
            new_nodes  = node_quote(md_block)
        elif block_type == BlockType.UNORDERED_LIST:
            new_nodes  = node_ul(md_block)
        elif block_type == BlockType.ORDERED_LIST:
            new_nodes  = node_ol(md_block)
        elif block_type == BlockType.PARAGRAPH:
            new_nodes  = node_paragraph(md_block)
        html_nodes.append(new_nodes)
    return ParentNode(tag="div", children=html_nodes)

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    new_nodes = []
    for text_node in text_nodes:
        new_child = text_node_to_html_node(text_node)
        new_nodes.append(new_child)
    return new_nodes

def node_heading(markdown):
    segments = markdown.split(" ",1)
    level = len(segments[0])
    tag = f"h{level}"
    text = segments[1]
    children = text_to_children(text)
    return ParentNode(tag=tag, children=children)

def node_code(markdown):
    text = markdown.strip("`")
    text = text.lstrip()
    text_node = TextNode(text, TextType.CODE)
    inner = text_node_to_html_node(text_node)
    return ParentNode(tag="pre", children=[inner])

def node_quote(markdown):
    lines = markdown.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].strip("> ")
    text = "".join(lines)
    children = text_to_children(text)
    return ParentNode(tag="blockquote", children=children)

def node_paragraph(markdown):
    markdown = markdown.replace("\n", " ")
    children = text_to_children(markdown)
    return ParentNode(tag="p", children=children)

def node_ul(markdown):
    items = []
    for line in markdown.split("\n"):
        text = line.lstrip("- ")
        items.append(text)
    children = list_items(items)
    return ParentNode(tag="ul", children=children)

def node_ol(markdown):
    items = []
    for line in markdown.split("\n"):
        text = line.lstrip("1234567890. ")
        items.append(text)
    children = list_items(items)
    return ParentNode(tag="ol", children=children)

def list_items(items):
    children = []
    for text in items:
        subnodes = text_to_children(text)
        new_node = ParentNode(tag="li", children=subnodes)
        children.append(new_node)
    return children