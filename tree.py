# Small script to print out the AST of a python source file. Takes the path of
# the file, parses the source code and prints out the generated syntaxe tree.

import ast
import sys
import json

def get_ast(file_path: str, as_json=False):
    with open(file_path, 'r') as file:
        source = file.read()
    tree = ast.parse(source)
    if as_json:
        dict_tree = ast_to_dict(tree)
        return json.dumps(dict_tree, indent=2)

    return ast.dump(tree)


def ast_to_dict(node):
    if isinstance(node, ast.AST):
        fields = {}
        for field, value in ast.iter_fields(node):
            fields[field] = ast_to_dict(value)
        return {
            "ast_type": type(node).__name__,
            "fields": fields
        }
    elif isinstance(node, list):
        return [ast_to_dict(item) for item in node]
    return node



if __name__ == '__main__':
    if not len(sys.argv) >= 2:
        print('Wrong number of argument.\nUsage: python tree.py <file_path> [--json]')
        sys.exit(1)

    file_path = sys.argv[1]
    as_json = "--json" in sys.argv
    out = get_ast(file_path, as_json)
    print(out)
