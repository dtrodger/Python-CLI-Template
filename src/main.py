from __future__ import annotations
import logging
import click


log = logging.getLogger(__name__)


@click.command()
@click.option(
    "-e", "--env", default="dev", help="env environment alias", type=str,
)
def foo(env: str) -> None:
    pass


@click.group()
def cli() -> None:
    pass


def main() -> None:
    commands = [
        foo
    ]
    for command in commands:
        cli.add_command(command)

    cli()


if __name__ == "__main__":
    main()
