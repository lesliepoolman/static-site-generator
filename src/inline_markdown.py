import re
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.texttype != "text":
            result.append(node)
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("Invalid Markdown, missing closing delimiter")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(split_text[i], "text"))
            else:
                result.append(TextNode(split_text[i], text_type))
    return result

def extract_markdown_images(text):
    return re.findall(r"", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)