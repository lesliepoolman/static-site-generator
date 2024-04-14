import unittest

from textnode import TextNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode("This is text with a **bolded** word and **another**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode("This is text with a **bolded word** and **another**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded word", "bold"),
                TextNode(" and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_extract_images_using_regex(self):
        example = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        )
        exp_res = [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("another", "https://i.imgur.com/dfsdkjfd.png"),
        ]
        self.assertEqual(exp_res, example)

    def test_extract_links_using_regex(self):
        example = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        )
        exp_res = [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another"),
        ]
        self.assertEqual(exp_res, example)

    def test_split_nodes_image_with_images(self):
        example = split_nodes_image(
            [
                TextNode(
                    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    "text",
                )
            ]
        )
        exp_res = [
            TextNode("This is text with an ", "text"),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text"),
            TextNode(
                "second image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
        ]
        self.assertEqual(exp_res, example)

    def test_split_nodes_image_with_images2(self):
        example = split_nodes_image(
            [
                TextNode(
                    "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and this is for confusion",
                    "text",
                )
            ]
        )
        exp_res = [
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and this is for confusion", "text"),
        ]
        self.assertEqual(exp_res, example)

    def test_split_nodes_image_without_images(self):
        example = split_nodes_image([TextNode("This is text without images", "text")])
        exp_res = [
            TextNode("This is text without images", "text"),
        ]
        self.assertEqual(exp_res, example)

    def test_split_nodes_link_with_links(self):
        example = split_nodes_link(
            [
                TextNode(
                    "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    "text",
                )
            ]
        )
        exp_res = [
            TextNode("This is text with an ", "text"),
            TextNode(
                "link",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and another ", "text"),
            TextNode(
                "second link",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
            ),
        ]
        self.assertEqual(exp_res, example)

    def test_split_nodes_link_with_links2(self):
        example = split_nodes_link(
            [
                TextNode(
                    "[link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and over here too.",
                    "text",
                )
            ]
        )
        exp_res = [
            TextNode(
                "link",
                "link",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and over here too.", "text"),
        ]
        self.assertEqual(exp_res, example)

    def test_split_nodes_link_without_links(self):
        example = split_nodes_link([TextNode("This is text without links", "text")])
        exp_res = [
            TextNode("This is text without links", "text"),
        ]
        self.assertEqual(exp_res, example)

    def test_text_to_textnodes(self):
        example = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        exp_res = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode(
                "image",
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
            ),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(exp_res, example)



if __name__ == "__main__":
    unittest.main()
