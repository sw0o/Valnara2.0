import requests
import re
from rich.console import Console
from rich.prompt import Prompt
from Banner import display_banner
from WordPress_Detection import Is_WordPress    
c = Console()

display_banner()

def Valid_Format(URL): #
    Blocked_Domains = {".mil", ".gov", ".edu"}
    r = r"^(https?://)([a-zA-Z0-9\u00a1-\uffff-]+\.)+(com|org|net|edu|tech|gov|mil|info|biz|name|pro|xyz|xn--[a-zA-Z0-9-]+\.[a-zA-Z]{2,})(\/[^\s]*)?$"
    if any(domain in URL for domain in Blocked_Domains):
        c.print("[bold red]Blocked Domain[/bold red]")    
        return "Blocked Domain"
    match = re.match(r, URL)
    if match is not None:
        return "Valid URL"
    else:
        c.print("[red]Invalid URL[/red]")
        return "Invalid URL"

def Check_Presence(url):  #
    try:
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            return  "Website is reachable"
        else: 
            c.print("[red]URL is not reachable[/red]")
    except requests.exceptions.Timeout:
        c.print("[red]The request timed out.[/red]")
    except requests.exceptions.ConnectionError:
        c.print("[red] DNS OR NETWORK ISSUE.[/red]")
    except requests.exceptions.RequestException as e:
        c.print(f"[red]An error occurred: {e}[/red]")

try: 
    URL = Prompt.ask("[bold blue]Enter the URL: \n[/bold blue]")
    Valid_Format_Result = Valid_Format(URL)  
except KeyboardInterrupt: 
    print("\nKeyboardInterrupt has been caught.")

################### controllers ###################
if Valid_Format_Result == "Valid URL":
    Precense_Result = Check_Presence(URL)
    if Precense_Result == "Website is reachable":
        WordPress_Result = Is_WordPress(URL)
        if WordPress_Result == "WordPress  Detected":
            c.print("[bold green] WordPress Detected[/bold green]")
        else :
            c.print("[bold red] WordPress Not Detected[/bold red]")
