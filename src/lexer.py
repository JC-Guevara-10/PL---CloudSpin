import re

TOKEN_DEFINITIONS = [
    ("SPIN UP",        r"^SPIN UP\b"),
    ("SCALE",          r"^SCALE\b"),
    ("WAIT UNTIL",     r"^WAIT UNTIL\b"),
    ("SPIN DOWN",      r"^SPIN DOWN\b"),
    ("PARSE",          r"^PARSE\b"),
    ("EXECUTE",        r"^EXECUTE\b"),
    ("LOG",            r"^LOG\b"),
    ("TERMINATE",      r"^TERMINATE\b"),
]

def lexer(user_input: str) -> dict | None:
    """
    LEXER — Tokenizes the raw input string.

    Scans the uppercased input against each regex pattern.
    Returns a token dict like {"keyword": "SPIN UP"} if matched,
    or None if no pattern matches.
    """
    normalized = user_input.strip().upper()

    for keyword, pattern in TOKEN_DEFINITIONS:
        if re.match(pattern, normalized):
            token = {"keyword": keyword}
            return token

    return None  # No valid token found