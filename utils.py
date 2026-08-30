# rag_utils.py
def _word_chunker(text, chunk_size, overlap):
    words = text.split()
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be > overlap")
    chunks = []
    i = 0
    while i < len(words):
        end = min(i + chunk_size, len(words))
        chunks.append(" ".join(words[i:end]))
        i = end - overlap
    return chunks


try:
    import tiktoken


    def split_into_chunks(text, chunk_size=800, overlap=120, model="gpt-4o-mini"):
        """
        Token-based chunking (preferred). chunk_size and overlap are token counts.
        Requires tiktoken: pip install tiktoken
        """
        enc = tiktoken.encoding_for_model(model)
        tokens = enc.encode(text)
        if chunk_size <= overlap:
            raise ValueError("chunk_size must be > overlap")
        chunks = []
        step = chunk_size - overlap
        for i in range(0, len(tokens), step):
            chunk_tokens = tokens[i: i + chunk_size]
            chunks.append(enc.decode(chunk_tokens))
        return chunks

except Exception:
    # fallback to word-based chunking (chunk_size and overlap are word counts)
    def split_into_chunks(text, chunk_size=200, overlap=40, **_):
        """
        Fallback word-based chunking. Defaults chosen so behavior is similar.
        """
        return _word_chunker(text, chunk_size, overlap)
