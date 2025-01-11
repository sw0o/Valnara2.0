import pyfiglet
from rich.console import Console
from rich.progress import Progress
from time import sleep

c = Console()

def display_banner():
    banner = pyfiglet.figlet_format("V A L N A R A", font="slant")
    c.print(f"[magenta]{banner}[/magenta]")
    c.print("[bold green]$----------------------------------------------------------$[/bold green]")

    with Progress(
        "[progress.description]{task.description}",
        transient=True,
        expand=True,
        console=c,
    ) as progress:
        task = progress.add_task("[bold cyan]Initializing kernel modules...[/bold cyan]", total=100)
        for i in range(10):
            sleep(0.2)
            progress.update(task, advance=10)

    c.print("[bold green]>> System Ready: Modules Loaded Successfully![/bold green]")
    c.print("[bold green]>> Boot Sequence Completed. Launching Analysis Tools...[/bold green]")


