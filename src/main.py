from textnode import TextNode
from htmlnode import HTMLNode

def main():
    textnode = TextNode("This is a text node", "bold", "https://example.com")
    htmlnode = HTMLNode("table")
    child = HTMLNode("thead", "header")
    child.add_props({ "scope": "col" })
    htmlnode.add_child(child)
    htmlnode.add_props({ "class": "table", "id": "tester"})
    print(textnode)
    print(htmlnode)
    print(htmlnode.props_to_html())

main()