# Code Notes CLI

A simple command line tool to manage your notes using your favourite code editor and terminal. If like me, you love your code editor and would like a simple light-weight tool to manage your notes, this is for you!

## Why not just obsidian or some other note taking app?
If you are a coder, you already have the perfect tool for editing markdown files - your code editor! After years of playing with several note taking apps, I have realized that all you need is the following:
1. An easy way to create a new daily note (timestamped with today's date) for daily journaling
2. A quick way to add a short note to your daily note from the terminal
3. A handy way to open your notes directory in your code editor

With these basic command line functions, you can simply use the powerful search and editing features of your favorite editor (like Zed or VSCode) to manage your notes!

## Features

```
Usage: cnote [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  date         Prints the current date
  log          Create daily log
  log-meeting  Create meeting log
  log-project  Create project log
  new          Create a new note
  newday       Create a new note for a specific date
  quick        Add a quick note to today's note
  rmdays       Remove the symlinks for today, yesterday, and tomorrow
  today        Create a new note for today
  tomorrow     Create a new note for tomorrow
  vscode       Open the notes directory in VSCode
  yesterday    Create a new note for yesterday
  zed          Open the notes directory in Zed
```

See the Usage section below for more details.

## Installation

- First install `uv` as per instructions at [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

- Clone this repository and run the following commands:
  ```bash
  uv sync
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

- Test the installation by running `cnote` which should print a welcome message.

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
  cnote new projects/my_project
  ```
  This will create a new note in `./projects/` directory (created if it doesn't exist) with the name `my_project.md`. If name is not provided (so just `cnote new`) it would create a new note with timestamp as the filename in`./` directory.

- Start a new meeting log:
  ```bash
  cnote log-meeting meeting_name
  ```
  This will create a new `./meetings/meeting_name.md` file if it doesn't exist and add a new heading with today's date. If the file already exists, and contains log entries from previous days, it will prepend a new heading with today's date where you can enter today's log entries.

- Start a new project log:
  ```bash
  cnote log-project my_project
  ```
  This will create a new `./projects/my_project/log.md` file if it doesn't exist and add a new heading with today's date. If the file already exists, and contains log entries from previous days, it will prepend a new heading with today's date where you can enter today's log entries.

- Start a new daily log in any directory:
  ```bash
  cnote log relative/path/to/directory
  ```
  This will create a new `./relative/path/to/directory/log.md` file in a directory of your choice. In fact, `log-project` command above is equivalent to the following:
  ```bash
  cnote log projects/my_project
  ```

## Pro Usage

Code Notes CLI is built with Python using the awesome [click](https://click.palletsprojects.com/en/stable/) library. The entire code is in a single Python file (`cli.py`) and is under 200 lines of code. Need a new functionality or want to tweak the existing features to your liking? Simply fork this repository and add a new python function to implement your feature or update the existing ones in `cli.py`.
