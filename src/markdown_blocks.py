
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for chunk in blocks:
        stripped_chunk = chunk.strip()
        if not stripped_chunk: # This checks if stripped_chunk is an empty string
            # Empty after Stripping, so skip
            continue
        # Not empty, so add to clean_blocks
        clean_blocks.append(stripped_chunk)
    return clean_blocks

def block_to_block_type(block):
    headers = ['#', '##', '###', '####', '#####', '######']
    unordered = ['*', '-']
    order_list = 1
    bite = block.split('\n')
    if block.startswith(tuple(headers)):
        for i in bite:
            if not i.startswith(tuple(headers)):
                return block_type_paragraph
        return block_type_heading
    elif block.startswith('```') and block.endswith('```'):
        return block_type_code
    elif block.startswith(">"):
        for i in bite:
            if not i.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    elif block.startswith(tuple(unordered)):
        for i in bite:
            if not i.startswith(tuple(unordered)):
                return block_type_paragraph
        return block_type_ulist
    elif block.startswith('1. '):
        expected_number = 1
        for i in bite:
            checking = str(expected_number)+ '. '
            if i.startswith(checking):
                expected_number += 1
            else:
                return block_type_paragraph
        return block_type_olist
    else:
        return block_type_paragraph
    
