from rich.table import Table
from rich.console import Console

def print_Table(alias_list,alias):
    table = Table(title=alias)
    table.add_column("Alias", style="", no_wrap=True, justify="center")
    table.add_column("Definition", style="green", justify="center")
    for i in alias_list:
        table.add_row(i[0],i[1])
    console = Console()
    console.print(table)