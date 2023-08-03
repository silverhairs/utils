# Small script to print out the AST of a python source file. Takes the path of
# the file, parses the source code and prints out the generated syntaxe tree.

import ast
import sys
import json

def get_ast(file_path: str, as_json=False):
    with open(file_path, 'r') as file:
        source = file.read()
    tree = ast.parse(source)
    out = ast.dump(tree)

    if as_json:
        out = json.dumps(out, indent=2)
    return out



if __name__ == '__main__':
    if not len(sys.argv) > 2:
        print('Wrong number of argument.\nUsage: python tree.py <file_path> [--json]')
        sys.exit(1)

    file_path = sys.argv[1]
    as_json = "--json" in sys.argv
    out = get_ast(file_path, as_json)
    print(out)
