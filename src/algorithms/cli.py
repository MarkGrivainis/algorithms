"""Console script for tipseq_analysis."""
from typing import Optional

import click


@click.command()
def main(args: Optional[list[str]] = None) -> int:
    """Console script for tipseq_analysis."""
    click.echo(
        "Replace this message by putting your code into " "tipseq_analysis.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
