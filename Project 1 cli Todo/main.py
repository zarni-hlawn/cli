# This is the cli version of the "Project 1 cli Todo"
# Official Repository - https://github.com/zarni-hlawn/17

def main():
    Todo()


class Todo:
    def __init__(self):
        print(f"[bold magenta]Todo Is Now Running Successfully[/bold magenta]")
        print(f"[blue]Available Option 1. Read 2. Write 3 Update 4 Delete !Default is Read[/blue]", end='', sep='')
        while True:
            try:
                self.choice = float(input())
                break
            except ValueError:
                print(f"[bold red]Oops!  That was no valid Option.  Try again...[/bold red]")
        match self.choice:
            case 2:
                Write()
            case 3:
                Update()
            case 4:
                Delete()
            case _:
                Read()


class Read:
    def __init__(self):
        print(f"[bold magenta]Read Mode Activated[/bold magenta]")


class Write:
    def __init__(self):
        print(f"[bold magenta]Write Mode Activated[/bold magenta]")


class Update:
    def __init__(self):
        print(f"[bold magenta]Update Mode Activated[/bold magenta]")


class Delete:
    def __init__(self):
        print(f"[bold magenta]Delete Mode Activated[/bold magenta]")


if __name__ == "__main__":
    main()
