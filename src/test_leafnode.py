import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_repr_without_children(self):
        node = LeafNode("p", "Paragraph", {"class": "p"})
        expected_string = "tag=p | props={'class': 'p'} | value=Paragraph | children="
        self.assertEqual(str(node), expected_string)

    def test_props_to_html(self):
        node = LeafNode("p", "Paragraph", {"class": "paragraph", "id": "test_p"})
        self.assertEqual(node.props_to_html(), ' class="paragraph" id="test_p"')

    def test_props_to_html_guard(self):
        node = LeafNode("p")
        self.assertEqual(node.props_to_html(), "")

    def test_to_html(self):
        node = LeafNode("p", "Paragraph", {"class": "p", "id": "test_p"})
        self.assertEqual(node.to_html(), '<p class="p" id="test_p">Paragraph</p>')

    def test_to_html_without_value(self):
        node = LeafNode("p", None, {"class": "paragraph", "id": "test_p"})
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_without_tag(self):
        node = LeafNode(None, "Paragraph")
        self.assertEqual(node.to_html(), "Paragraph")


if __name__ == "__main__":
    unittest.main()
