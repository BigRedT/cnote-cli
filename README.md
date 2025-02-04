# Code Notes CLI

A simple command line tool to manage your notes using your favourite code editor.


```
Usage: cnote [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  date       Prints the current date
  new        Create a new note
  newday     Create a new note for a specific date
  quick      Add a quick note to today's note
  rmdays     Remove the symlinks for today, yesterday, and tomorrow
  today      Create a new note for today
  tomorrow   Create a new note for tomorrow
  vscode     Open the notes directory in VSCode
  yesterday  Create a new note for yesterday
  zed        Open the notes directory in Zed
```


## Installation

- First install `uv` as per instructions at [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

- Clone this repository and run the following commands:
  ```bash
  uv pip install -e .
  ```
  This would generate the `cnote` binary at `.venv/bin`

- Create a symlink to `.venv/bin/cnote` in a location that's added to your `PATH` variable. For example:
  ```bash
  ln -s /path/to/cnote-cli/.venv/bin/cnote /usr/local/bin/cnote
  ```

- Alternatively, instead of symlink, you can add the `.venv/bin` directory to your `PATH` variable like so:
  ```bash
  export PATH=$PATH:/path/to/cnote-cli/.venv/bin
  ```

- Finally, `cnote` uses the environment variable `CNOTE_DIR` to determine the directory where the notes are stored. You can set this variable in your `.bashrc` or `.zshrc` file like so:
  ```bash
  export CNOTE_DIR=/path/to/your/notes/directory
  ```
