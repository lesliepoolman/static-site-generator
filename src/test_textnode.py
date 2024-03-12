import unittest

from textnode import TextNode

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


if __name__ == "__main__":
    unittest.main()
