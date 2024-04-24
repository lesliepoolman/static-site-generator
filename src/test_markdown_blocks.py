import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        example = markdown_to_blocks(
            """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
                                     """
        )
        exp_res = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
        ]
        self.assertEqual(exp_res, example)

    def test_markdown_to_blocks_removes_blank_block(self):
        example = markdown_to_blocks(
            """
This is **bolded** paragraph




* This is a list
* with items
                                     """
        )
        exp_res = [
            "This is **bolded** paragraph",
            "* This is a list\n* with items",
        ]
        self.assertEqual(exp_res, example)

    def test_block_to_block_type_heading(self):
        example = block_to_block_type("# This is a heading")
        self.assertEqual(block_type_heading, example)

    def test_block_to_block_type_heading2(self):
        example = block_to_block_type("## This is a heading")
        self.assertEqual(block_type_heading, example)

    def test_block_to_block_type_heading3(self):
        example = block_to_block_type("### This is a heading")
        self.assertEqual(block_type_heading, example)

    def test_block_to_block_type_heading4(self):
        example = block_to_block_type("#### This is a heading")
        self.assertEqual(block_type_heading, example)

    def test_block_to_block_type_heading5(self):
        example = block_to_block_type("##### This is a heading")
        self.assertEqual(block_type_heading, example)

    def test_block_to_block_type_heading6(self):
        example = block_to_block_type("###### This is a heading")
        self.assertEqual(block_type_heading, example)

    def test_block_to_block_type_code(self):
        example = block_to_block_type("``` This is a code block")
        self.assertEqual(block_type_code, example)

    def test_block_to_block_type_quote(self):
        example = block_to_block_type("> This is a quote block")
        self.assertEqual(block_type_quote, example)

    def test_block_to_block_type_unordered_list(self):
        example = block_to_block_type("* This is an unordered list item")
        self.assertEqual(block_type_unordered_list, example)

    def test_block_to_block_type_unordered_list2(self):
        example = block_to_block_type("- This is an unordered list item")
        self.assertEqual(block_type_unordered_list, example)

    def test_block_to_block_type_ordered_list(self):
        example = block_to_block_type("1. This is an ordered list item")
        self.assertEqual(block_type_ordered_list, example)

    def test_block_to_block_type_ordered_list2(self):
        example = block_to_block_type("10. This is an ordered list item")
        self.assertEqual(block_type_ordered_list, example)

    def test_block_to_block_type_paragraph(self):
        example = block_to_block_type("This is a paragraph.")
        self.assertEqual(block_type_paragraph, example)


if __name__ == "__main__":
    unittest.main()
