# utils
A bunch of scripts to automate tasks I find myself doing more than once.

## Available scripts
- [tree](https://github.com/silverhairs/utils/blob/main/tree.py) : A python script that takes a python file path as an input, parses the code and prints out the AST. You can add the `--json` flag to get the output in a json format.
  > I usually use this with [tee](https://en.wikipedia.org/wiki/Tee_(command)) when I want the AST in a json file -> `python tree.py tree_example.py --json | tee ast.json`
