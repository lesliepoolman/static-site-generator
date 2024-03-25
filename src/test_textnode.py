import unittest

from leafnode import LeafNode
from textnode import (
        TextNode,
        text_type_to_tag
    )

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is node 1", "bold")
        node2 = TextNode("This is node 2", "bold")
        self.assertNotEqual(node, node2)

    def url_present_is_eq(self):
        node = TextNode("This is node 1", "italic", "https://sample.com")
        node2 = TextNode("This is node 1", "italic", "https://sample.com")
        self.assertEqual(node, node2)

    def url_present_not_eq(self):
        node = TextNode("Node 1", "italic", "https//:sample.com")
        node2 = TextNode("Node 1", "italic", "https//:sample2.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.sample.com")
        self.assertEqual("TextNode(This is a text node, text, https://www.sample.com)", repr(node))

    def test_text_node_to_html_node(self):
        for key in text_type_to_tag.keys():
            if key == "a":
                node = TextNode("Link", key, "https://www.sample.com")
                leaf = LeafNode(text_type_to_tag[key], "Link", { "href": node.url })
            elif key == "image":
                node = TextNode("Image", key, "https://www.source.com")
                leaf = LeafNode(text_type_to_tag[key], "", { "src": node.url, "alt": node.text })
            else:
                node = TextNode("Texty Node", key)
                leaf = LeafNode(text_type_to_tag[key], node.text)
            self.assertEqual(node.text_node_to_html_node().to_html(), leaf.to_html())

    def test_text_node_to_html_node_exception(self):
        node = TextNode("Texty Node", "table")
        with self.assertRaises(Exception) as ve:
            node.text_node_to_html_node()
            ve_error = ve.exception
            self.assertEqual(ve_error.error_code, "Invalid text type: table")



if __name__ == "__main__":
    unittest.main()
