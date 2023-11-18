def split_message(text, chunk_size=1900):
    """
    Splits a long message into chunks of a specified size.

    :param text: The text to be split.
    :param chunk_size: Maximum size of each chunk. Default is 1900.
    :return: A list of text chunks.
    """
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    while text:
        # If the remaining text is within the chunk size, add it and break
        if len(text) <= chunk_size:
            chunks.append(text)
            break

        # Find the nearest space to split the text
        nearest_space = text.rfind(' ', 0, chunk_size)
        if nearest_space == -1:
            # If no space found, just hard split
            nearest_space = chunk_size

        chunk, text = text[:nearest_space], text[nearest_space + 1:]
        chunks.append(chunk)

    return chunks
