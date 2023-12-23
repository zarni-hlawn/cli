# This is the cli version of the "Project 0 cli Calculator" 
# Official Repository - https://github.com/zarni-hlawn/cli 

from rich import print


def main():
    Calculator()


class Calculator:
    def __init__(self):
        print(f"[bold magenta]Calculator Is Now Running Successfully[/bold magenta] ~")
        Simple()


class Simple:
    def __init__(self):
        self.mode = "Simple"
        print(f"[bold magenta]Simple Mode Activated[/bold magenta]")
        print(f"[blue]available operators {operators}[/blue]")
        while True:
            try:
                print(f"[green]Enter your first number: [/green]", end='', sep='')
                self.first_number = float(input())
                break
            except ValueError:
                print(f"[bold red]Oops!  That was no valid number.  Try again...[/bold red]")
        while True:
            print(f"[green]enter operator: [/green]", end='', sep='')
            self.operator = str(input())
            if self.operator in operators:
                break
            else:
                print(f"[bold red]Oops!  That was no valid operator.  Try again...[/bold red]")
        while True:
            try:
                print(f"[green]enter your second number: [/green]", end='', sep='')
                self.second_number = float(input())
                break
            except ValueError:
                print(f"[bold red]Oops!  That was no valid number.  Try again...[/bold red]")
        self.calculate()

    def calculate(self):
        result = None
        match self.operator:
            case '+':
                result = self.first_number + self.second_number
                print(f"[bold green]Result: {result}[/bold green]")
            case '-':
                result = self.first_number - self.second_number
                print(f"[bold green]Result: {result}[/bold green]")
            case '*':
                result = self.first_number * self.second_number
                print(f"[bold green]Result: {result}[/bold green]")
            case '/':
                if self.second_number != 0:
                    result = self.first_number / self.second_number
                    print(f"[bold green]Result: {result}[/bold green]")
                else:
                    print(f"[bold red]Error: Division by zero.[/bold red]")
            case '%':
                if self.second_number != 0:
                    result = self.first_number % self.second_number
                    print(f"[bold green]Result: {result}[/bold green]")
                else:
                    print(f"[bold red]Error: Division by zero.[/bold red]")
            case _:
                print(f"[bold red]Oops!  Unexpected Error.  Try again...[/bold red]")


if __name__ == "__main__":
    operators = ["+", "-", "*", "/", "%"]
    main()
