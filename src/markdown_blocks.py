block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

block_type_from_md_tag = {
    "#": block_type_heading,
    "##": block_type_heading,
    "###": block_type_heading,
    "####": block_type_heading,
    "#####": block_type_heading,
    "######": block_type_heading,
    "```": block_type_code,
    ">": block_type_quote,
    "*": block_type_unordered_list,
    "-": block_type_unordered_list,
}

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        if block == "":
            continue
        clean_block = block.strip()
        blocks.append(clean_block)
    return blocks

def block_to_block_type(block):
    md_tag = block.split()[0]
    if md_tag in block_type_from_md_tag.keys():
        return block_type_from_md_tag[md_tag]
    if md_tag[-1] == "." and any(c.isdigit() for c in md_tag[:-1]):
        return block_type_ordered_list
    return block_type_paragraph