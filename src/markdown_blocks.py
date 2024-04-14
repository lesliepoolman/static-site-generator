def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        if block == "":
            continue
        clean_block = block.strip()
        blocks.append(clean_block)
    return blocks