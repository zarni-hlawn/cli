# This is the cli version of the "Project 1 cli Todo"
# Official Repository - https://github.com/zarni-hlawn/cli

from rich.console import Console

console = Console()


def main():
    todo()


def todo():
    console.print("[bold magenta]Todo Is Now Running Successfully[/bold magenta]")
    console.print("[blue]Available Options: 1. Read 2. Write 3. Update 4. Delete (Default is Read)[/blue]", end='',
                  sep='')

    while True:
        try:
            choice = float(input())
            break
        except ValueError:
            console.print("[bold red]Oops! That was not a valid option. Try again...[/bold red]")

    if choice == 2:
        write()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    else:
        read()


def autogenerate_number():
    numbers = []

    with open("records.csv", "r") as file:
        for record in file:
            number, title, context = record.rstrip().split(",")
            numbers.append(int(number))

        numbers = sorted(numbers)

    if numbers:
        new_number = max(numbers) + 1
        return new_number
    else:
        new_number = 1
        return new_number


def read():
    console.print("[bold magenta]Read Mode Activated[/bold magenta]")

    with open("records.csv") as file:
        for record in file:
            number, title, context = record.rstrip().split(",")
            console.print(f"number: {number}\ntitle: {title}\ncontext: {context}\n")


def write():
    console.print("[bold magenta]Write Mode Activated[/bold magenta]")

    console.print("[green]Enter title: [/green]", end='', sep='')
    title = str(input())
    console.print("[green]Enter context: [/green]", end='', sep='')
    context = str(input())
    number = autogenerate_number()

    with open("records.csv", "a") as file:
        file.write(f"{number},{title},{context}\n")
    console.print(f"[bold green]Success!![/bold green]")


def update():
    console.print("[bold magenta]Update Mode Activated[/bold magenta]")
    console.print("[green]Enter number: [/green]", end='', sep='')
    choice = int(input())

    with open("records.csv", "r") as file:
        lines = file.readlines()

    with open("records.csv", "w") as file:
        for line in lines:
            number, title, context = line.rstrip().split(",")
            if int(number) == choice:
                console.print("[green]Enter new title: [/green]", end='', sep='')
                new_title = input()
                console.print("[green]Enter new context: [/green]", end='', sep='')
                new_context = input()
                file.write(f"{number},{new_title},{new_context}\n")
            else:
                file.write(line)

    console.print("[bold green]Success!![/bold green]")


def delete():
    console.print("[bold magenta]Delete Mode Activated[/bold magenta]")
    console.print("[green]Enter number: [/green]", end='', sep='')
    choice = int(input())

    with open("records.csv", "r") as file:
        lines = file.readlines()

    with open("records.csv", "w") as file:
        for line in lines:
            number, _, _ = line.rstrip().split(",")
            if int(number) != choice:
                file.write(line)

    console.print(f"[bold green]Success!![/bold green]")


if __name__ == "__main__":
    main()
