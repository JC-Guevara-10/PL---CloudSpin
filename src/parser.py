def parser(token: dict | None) -> str | None:
    """
    PARSER — Validates and structures the token.

    Accepts the token produced by the lexer.
    Returns the keyword string if valid, or None if the token is malformed
    or missing.
    """
    if token is None:
        return None  # Lexer found no match

    if isinstance(token, dict) and "keyword" in token:
        return token["keyword"]  # Well-formed token, extract keyword

    return None  # Malformed token structure