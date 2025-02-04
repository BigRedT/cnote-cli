# Code Notes CLI

A simple command line tool to manage your notes using your favourite code editor. If like me, you love your code editor and would like a simple light-weight tool to manage your notes, this is for you!


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
  This would generate the `cnote` binary at `./.venv/bin`

- Create a symlink to `./.venv/bin/cnote` in a location that's added to your `PATH` variable. For example:
  ```bash
  ln -s /path/to/cnote-cli/.venv/bin/cnote /usr/local/bin/cnote
  ```
  This would allow you to run `cnote` from anywhere in your terminal.

- Alternatively, instead of symlink, you can add the `.venv/bin` directory to your `PATH` variable like so:
  ```bash
  export PATH=$PATH:/path/to/cnote-cli/.venv/bin
  ```

- Finally, `cnote` uses the environment variable `CNOTE_DIR` to determine the directory where the notes are stored. You can set this variable in your `.bashrc` or `.zshrc` file like so:
  ```bash
  export CNOTE_DIR=/path/to/your/notes/directory
  ```

- Make sure to run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

## Usage

All paths are relative to your `CNOTE_DIR` directory.

- To create a new note for today/yesterday/tomorrow, run:
  ```bash
  cnote today/yesterday/tomorrow
  ```
  This will create a markdown file with the day's date in `./daily/` and also create an easy to access symlink to the corresponding note in `./`.
- To open the notes directory in VSCode or Zed, run:
  ```bash
  cnote vscode/zed
  ```
- To add a quick note to today's note, run:
  ```bash
  cnote quick "Your quick note here"
  ```
  This will append the quick note to today's note with a timestamp.
- Create a new note:
  ```bash
  cnote new --name projects/my_project
  ```
  This will create a new note in `./projects/` directory (created if it doesn't exist) with the name `my_project.md`. If `--name` is note provided it would create a new note with timestamp as the filename in`./` directory.
