import re
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.texttype != "text":
            result.append(node)
            continue
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
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.texttype != "text":
            result.append(node)
            continue
        tuples = extract_markdown_images(node.text)
        if len(tuples) == 0:
            result.append(node)
            continue
        else:
            node_text = node.text
            for tup in tuples:
                txt_lst = node_text.split(f"![{tup[0]}]({tup[1]})", 1)
                if len(txt_lst) != 2:
                    raise Exception("Invalid Markdown, Image not properly closed")
                if txt_lst[0] != "":
                    result.append(TextNode(txt_lst[0], "text"))
                result.append(TextNode(tup[0], "image", tup[1]))
                node_text = txt_lst[1]
            if node_text != "":
                result.append(TextNode(node_text, "text"))
    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.texttype != "text":
            result.append(node)
            continue
        tuples = extract_markdown_links(node.text)
        if len(tuples) == 0:
            result.append(node)
            continue
        else:
            node_text = node.text
            for tup in tuples:
                txt_lst = node_text.split(f"[{tup[0]}]({tup[1]})", 1)
                if len(txt_lst) != 2:
                    raise Exception("Invalid Markdown, link not properly closed")
                if txt_lst[0] != "":
                    result.append(TextNode(txt_lst[0], "text"))
                result.append(TextNode(tup[0], "link", tup[1]))
                node_text = txt_lst[1]
            if node_text != "":
                result.append(TextNode(node_text, "text"))
    return result
