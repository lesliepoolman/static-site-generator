import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_with_child(self):
        node = HTMLNode("table")
        node2= HTMLNode("thead", "Header")
        node.add_props({ "class": "table" })
        node2.add_props({ "scope": "col" })
        node.add_child(node2)
        expected_string = "tag=table | props={'class': 'table'} | value=None | children="
        expected_string += f"\n->-> tag=thead | props={{'scope': 'col'}} | value=Header | children="
        self.assertEqual(str(node), expected_string)

if __name__ == "__main__":
    unittest.main()
