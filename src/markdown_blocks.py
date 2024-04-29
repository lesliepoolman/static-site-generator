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
    lines = block.split("\n")
    md_tag = block.split()[0]
    result = block_type_paragraph
    if md_tag[-1] == "." and any(c.isdigit() for c in md_tag[:-1]):
        for line in lines:
            line_tag = line.split()[0]
            if line_tag[-1] == "." or any(c.isdigit() for c in line_tag[:-1]):
                result = block_type_ordered_list
            else:
                return block_type_paragraph
    elif md_tag in block_type_from_md_tag.keys():
        if "#" in md_tag or block_type_from_md_tag[md_tag] == block_type_code and lines[-1] == md_tag:
            result = block_type_from_md_tag[md_tag]
        elif (
            block_type_from_md_tag[md_tag] == block_type_quote
            or block_type_from_md_tag[md_tag] == block_type_unordered_list
        ):
            for line in lines:
                if line.split()[0] == md_tag:
                    result = block_type_from_md_tag[md_tag]
                else:
                    return block_type_paragraph
    return result
