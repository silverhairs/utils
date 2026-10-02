# utils
A bunch of scripts to automate tasks I find myself doing more than once.

## Available scripts
- [tree](https://github.com/silverhairs/utils/blob/main/tree.py) : A python script that takes a python file path as an input, parses the code and prints out the AST. You can add the `--json` flag to get the output in a json format.
  > I usually use this with [tee](https://en.wikipedia.org/wiki/Tee_(command)) when I want the AST in a json file -> `python tree.py tree_example.py --json | tee ast.json`

- [teams_keep_active](https://github.com/silverhairs/utils/blob/main/teams_keep_active.py) : Prevents Microsoft Teams from marking you as idle by simulating subtle mouse movements at regular intervals. Useful when you need to stay "active" on Teams while stepping away from your computer.
  ```bash
  # Install dependencies first (macOS)
  pip install pyautogui pyobjc-core pyobjc

  # Run with default 4-minute interval
  python teams_keep_active.py

  # Run with custom interval (e.g., 3 minutes)
  python teams_keep_active.py --interval 180
  ```
  > **Note**: Teams typically marks users as idle after 5 minutes of inactivity. The default interval of 4 minutes ensures you stay active. Press Ctrl+C to stop the script.
