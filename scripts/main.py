import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.lexer import lexer
from src.parser import parser
from src.interpreter import interpreter

def main():
    print("=" * 55)
    print("  DEPLOYMENT KEYWORD INTERPRETER")
    print("=" * 55)
    print("Valid keywords: SPIN UP, SCALE, WAIT UNTIL, SPIN DOWN,")
    print("                PARSE, EXECUTE, LOG, TERMINATE")
    print("=" * 55)

    while True:
        user_input = input("\nEnter a keyword: ")

        # Stage 1: LEXER — tokenize the input
        token = lexer(user_input)

        # Stage 2: PARSER — validate the token
        keyword = parser(token)

        # Stage 3: INTERPRETER — get the meaning
        if keyword:
            meaning = interpreter(keyword)
            print(f"\n  [{keyword}] → {meaning}")
            print()
            break
        else:
            print("  ✗ Invalid keyword. Please try again.")


if __name__ == "__main__":
    main()