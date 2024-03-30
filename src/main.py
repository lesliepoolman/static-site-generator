from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode


def main():
    node = ParentNode(
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        "p",
    )

    print(node.to_html())


main()
