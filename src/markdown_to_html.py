from htmlnode import LeafNode, ParentNode, HTMLNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from markdown_blocks import (
    markdown_to_blocks, 
    block_to_block_type, 
    block_type_code, 
    block_type_heading, 
    block_type_olist, 
    block_type_paragraph, 
    block_type_quote, 
    block_type_ulist,
)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def block_to_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    new_node = ParentNode('p', children)
    return new_node

def block_to_header(block):
    if block.startswith("######"):
        tag = "h6"
    elif block.startswith("#####"):
        tag = "h5"
    elif block.startswith("####"):
        tag = "h4"
    elif block.startswith("###"):
        tag = "h3"
    elif block.startswith("##"):
        tag = "h2"
    elif block.startswith("#"):
        tag = "h1"
    cleaned = block.lstrip(" #")
    children = text_to_children(cleaned)
    new_node = ParentNode(tag, children)
    return new_node

def block_to_blockquote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    new_node = ParentNode("blockquote", children)
    return new_node

def block_to_ulist(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        cleaned = item[2:]
        children = text_to_children(cleaned)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def block_to_olist(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        cleaned = item[3:]
        children = text_to_children(cleaned)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def block_to_code(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", code)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return block_to_paragraph(block)
    if block_type == block_type_heading:
        return block_to_header(block)        
    if block_type == block_type_quote:
        return block_to_blockquote(block)
    if block_type == block_type_ulist:
        return block_to_ulist(block)
    if block_type == block_type_olist:
        return block_to_olist(block)
    if block_type == block_type_code:
        return block_to_code(block)