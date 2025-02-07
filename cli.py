import datetime
import os

import click


@click.group(invoke_without_command=True)
@click.pass_context
def cnote(ctx):
    cnote_dir = os.getenv("CNOTE_DIR", os.path.expanduser("~/.cnote"))
    os.makedirs(cnote_dir, exist_ok=True)
    ctx.obj = dict(cnote_dir=cnote_dir)
    if ctx.invoked_subcommand is None:
        click.echo("Welcome to CodeNotes!")
        click.echo(f"Your notes are located at {ctx.obj['cnote_dir']}")
        click.echo(
            "To change this, set the CNOTE_DIR environment variable to your notes directory."
        )


def create_daily_note(
    ctx, note_date: datetime.date, symlink_name: str | None = None
):
    cnote_dir = ctx.obj["cnote_dir"]
    daily_notes_dir = os.path.join(cnote_dir, "daily")
    note_path = os.path.join(daily_notes_dir, f"{note_date}.md")
    if not os.path.exists(note_path):
        os.makedirs(daily_notes_dir, exist_ok=True)
        with open(note_path, "w") as f:
            f.write(f"# Daily note: {note_date}\n")
        click.echo(f"Created note at {note_path}")
    else:
        click.echo(f"Note already exists at {note_path}")

    if symlink_name is not None:
        symlink_path = os.path.join(cnote_dir, symlink_name)
        if os.path.islink(symlink_path) or os.path.exists(symlink_path):
            os.remove(symlink_path)
        os.symlink(note_path, symlink_path)


@cnote.command(help="Create a new note for today")
@click.pass_context
def today(ctx):
    today = datetime.date.today()
    create_daily_note(ctx, today, symlink_name="today.md")


@cnote.command(help="Create a new note for yesterday")
@click.pass_context
def yesterday(ctx):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    create_daily_note(ctx, yesterday, symlink_name="yesterday.md")


@cnote.command(help="Create a new note for tomorrow")
@click.pass_context
def tomorrow(ctx):
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(days=1)
    create_daily_note(ctx, yesterday, symlink_name="tomorrow.md")


@cnote.command(help="Remove the symlinks for today, yesterday, and tomorrow")
@click.pass_context
def rmdays(ctx):
    cnote_dir = ctx.obj["cnote_dir"]
    for day in ["yesterday", "tomorrow", "today"]:
        symlink_path = os.path.join(cnote_dir, f"{day}.md")
        if os.path.islink(symlink_path) or os.path.exists(symlink_path):
            os.remove(symlink_path)


@cnote.command(help="Prints the current date")
@click.pass_context
def date(ctx):
    today = datetime.date.today()
    click.echo(today)


@cnote.command(help="Add a quick note to today's note")
@click.argument("note")
@click.pass_context
def quick(ctx, note: str):
    today = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    create_daily_note(ctx, today, symlink_name="today.md")
    todays_note_path = os.path.join(ctx.obj["cnote_dir"], f"daily/{today}.md")
    add_quick_note_header = False
    is_last_char_newline = False
    with open(todays_note_path, "r") as f:
        content = f.read()
        if "# Quick notes" not in content:
            add_quick_note_header = True

        if len(content) > 0 and content[-1] == "\n":
            is_last_char_newline = True

    with open(todays_note_path, "a") as f:
        if add_quick_note_header:
            f.write("\n\n---\n\n# Quick notes\n\n")

        if not is_last_char_newline:
            f.write("\n")

        f.write(f"- {time} - {note}")


@cnote.command(help="Create a new note for a specific date")
@click.argument("year", type=int)
@click.argument("month", type=int)
@click.argument("day", type=int)
@click.pass_context
def newday(ctx, year, month, day):
    try:
        note_date = datetime.date(year, month, day)
    except ValueError:
        note_date = None
        click.echo("Invalid date")
        ctx.exit(1)

    if isinstance(note_date, datetime.date):
        create_daily_note(ctx, note_date)


@cnote.command(help="Create a new note")
@click.argument(
    "name",
    type=str,
    default=datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
)
@click.pass_context
def new(ctx, name):
    cnote_dir = ctx.obj["cnote_dir"]
    dirname = os.path.dirname(name)
    dirpath = os.path.join(cnote_dir, dirname)
    os.makedirs(dirpath, exist_ok=True)
    fname = os.path.basename(name)
    fpath = os.path.join(dirpath, f"{fname}.md")
    os.system(f"touch {fpath}")
    click.echo(f"Created note at {fpath}")


@cnote.command(help="Open the notes directory in Zed")
@click.pass_context
def zed(ctx):
    cnote_dir = ctx.obj["cnote_dir"]
    os.system(f"zed {cnote_dir}")


@cnote.command(help="Open the notes directory in VSCode")
@click.pass_context
def vscode(ctx):
    cnote_dir = ctx.obj["cnote_dir"]
    os.system(f"code {cnote_dir}")


if __name__ == "__main__":
    cnote()
