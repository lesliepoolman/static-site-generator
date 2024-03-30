from leafnode import LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.texttype != "text":
            result.append(node)
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("Invalid Markdown, missing closing delimiter")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(split_text[i], "text"))
            else:
                result.append(TextNode(split_text[i], text_type))
    return result

text_type_to_tag = {
    "bold": "b",
    "italic": "i",
    "code": "code",
    "link": "a",
    "image": "img",
    "text": None,
}
class TextNode():
    def __init__(self, text, texttype, url=None):
        self.text = text
        self.texttype = texttype
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.texttype == other.texttype and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.texttype}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.texttype not in text_type_to_tag.keys():
            raise Exception(f"Invalid text type: {self.texttype}")
        elif self.texttype == "image":
            return LeafNode(text_type_to_tag[self.texttype], "", { "src": self.url, "alt": self.text })
        elif self.texttype == "a":
            return LeafNode(text_type_to_tag[self.texttype], self.text, { "href": self.url })
        else:
            return LeafNode(text_type_to_tag[self.texttype], self.text)