import click
from tabulate import tabulate

from parametric_svg_utility import utils


@click.group()
@click.version_option()
def cli():
    """Apply transformations to Parametric SVG files"""


# See docs at https://zetcode.com/python/click/

# Commands:
# - tabulate params
# - add a g element and transformation around files
# - apply substitution into formulae
# - substitute in params [either defaults or new]


@cli.command()
@click.argument("input_files", type=click.File("rb"), nargs=-1, required=True)
@click.option('-c', '--csv', help='Format output as CSV, rather than pretty-printed table')
@click.option('--full-name/--short-name', help='Show full file path as provided as argument, or just file name',
              required=False, default=False)
def parameters(input_files, csv, full_name):
    """List parameters and their default values"""

    fieldnames, rows = utils.tabulate_params(input_files, full_name)

    if csv:
        print(",".join(fieldnames))
        for row in rows:
            vals = [row.get(k, "") for k in fieldnames]
            print(",".join(vals))
    else:
        table = []
        for row in rows:
            vals = [row.get(k, "") for k in fieldnames]
            table.append(vals)

        print(tabulate(table, headers=fieldnames))
