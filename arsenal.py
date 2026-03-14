import click
import os
import sys
from core.loader import ToolLoader
from core.installer import ToolInstaller
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    """⚔️ RedTeam-Arsenal: The Ultimate APT & Red Team Toolkit for Single Combat."""
    pass

@cli.command()
def list_tools():
    """List all available tools in the arsenal."""
    loader = ToolLoader()
    tools = loader.get_all_tools()
    
    table = Table(title="RedTeam-Arsenal Tool Catalog", show_header=True, header_style="bold magenta")
    table.add_column("Category", style="cyan", width=20)
    table.add_column("Tool Name", style="green")
    table.add_column("Version", style="yellow")
    table.add_column("Description", style="white")

    for category, tool_list in tools.items():
        for tool in tool_list:
            table.add_row(category, tool['name'], tool.get('version', 'N/A'), tool.get('description', 'No description.'))
    
    console.print(table)

@cli.command()
@click.argument('category')
@click.argument('tool_name')
def install(category, tool_name):
    """Install a specific tool. Example: install recon subfinder"""
    installer = ToolInstaller()
    installer.install(category, tool_name)

@cli.command()
def gui():
    """Launch the RedTeam-Arsenal GUI."""
    console.print("[bold blue]Launching RedTeam-Arsenal GUI...[/bold blue]")
    os.chdir("gui")
    os.system("python3 app.py")

if __name__ == '__main__':
    cli()
