import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_with_child(self):
        node2= HTMLNode("thead", "Header", None, { "scope": "col" })
        node = HTMLNode("table", None, [node2], { "class": "table" })
        expected_string = "tag=table | props={'class': 'table'} | value=None | children="
        expected_string += f"\n->-> tag=thead | props={{'scope': 'col'}} | value=Header | children="
        self.assertEqual(str(node), expected_string)

    def test_props_to_html(self):
        node = HTMLNode("table", None, None, { "class": "table", "id": "test_table" })
        self.assertEqual(node.props_to_html(), " class=\"table\" id=\"test_table\"")

    def test_props_to_html_guard(self):
        node = HTMLNode("table")
        self.assertIsNone(node.props_to_html())

if __name__ == "__main__":
    unittest.main()
