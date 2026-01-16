from core.lexer import Lexer
from parsing.parser import Parser
from runtime.interpreter import Interpreter
from runtime.context import Context
from runtime.builtins import global_symbol_table
import sys
import os



def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 gpl.py <filename>.kalang")
        return

    filepath = sys.argv[1]

    if not filepath.endswith(".kalang"):
        print("Error: The input file must have a .kalang extension.")
        return

    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        return

    try:
        with open(filepath, 'r') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if text.strip() == "":
        return

    result, error = run(filepath, text)

    if error:
        print(error.as_string())


if __name__ == '__main__':
    main()