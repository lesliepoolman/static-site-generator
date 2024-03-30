import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            "p",
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_props(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text", {"id": "italy"}),
                LeafNode(None, "Normal text"),
            ],
            "p",
            {"class": "p"},
        )
        self.assertEqual(
            node.to_html(),
            '<p class="p"><b>Bold text</b>Normal text<i id="italy">italic text</i>Normal text</p>',
        )

    def test_to_html_with_parent(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            "p",
            {"class": "p"},
        )
        node2 = ParentNode([node], "div", {"class": "container"})
        self.assertEqual(
            node2.to_html(),
            '<div class="container"><p class="p"><b>Bold text</b>Normal text</p></div>',
        )

    def test_to_html_with_no_children(self):
        node = ParentNode(None, "p", {"class": "p"})
        with self.assertRaises(ValueError) as ve:
            node.to_html()
            ve_error = ve.exception
            self.assertEqual(ve_error.error_code, "Children cannot be None")

    def test_to_html_with_no_tag(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            None,
            {"class": "p"},
        )
        with self.assertRaises(ValueError) as ve:
            node.to_html()
            ve_error = ve.exception
            self.assertEqual(ve_error.error_code, "Tag cannot be None")


if __name__ == "__main__":
    unittest.main()
