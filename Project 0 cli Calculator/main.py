# This is the cli version of the "Project 0 Calculator"

from rich import print


def main():
    Calculator()


class Calculator:
    def __init__(self):
        print(f"[bold magenta]Calculator[/bold magenta] Is Now Running Successfully ~")
        while True:
            try:
                self.choice = float(input(f"1. Simple 2. Scientific 3. Date  !Default is 'Simple'"))
                break
            except ValueError:
                print(f"[red]Oops!  That was no valid number.  Try again...[/red]")
        match self.choice:
            case 1:
                Simple()
            case 2:
                Converter()
            case 3:
                Date()
            case _:
                print(f"[red]Oops!  That was no valid options.  Try again...[/red]")


class Simple:
    def __init__(self):
        self.mode = "Simple"
        print(f"Simple Mode Activated")
        while True:
            try:
                self.first_number = float(input(f"enter your first number: "))
                break
            except ValueError:
                print(f"[red]Oops!  That was no valid number.  Try again...[/red]")
        while True:
            self.operator = str(input(f"enter operator: "))
            if self.operator in operators:
                break
            else:
                print(f"[red]Oops!  That was no valid operator.  Try again...[/red]")
        while True:
            try:
                self.second_number = float(input(f"enter your second number: "))
                break
            except ValueError:
                print(f"[red]Oops!  That was no valid number.  Try again...[/red]")
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
                    print(f"Error: Division by zero.")
            case '%':
                if self.second_number != 0:
                    result = self.first_number % self.second_number
                    print(f"[bold green]Result: {result}[/bold green]")
                else:
                    print(f"Error: Division by zero.")
            case _:
                print(f"[red]Oops!  Unexpected Error.  Try again...[/red]")


class Converter:
    def __init__(self):
        print(f"Converter Mode Activated")


class Date:
    def __init__(self):
        self.result = None
        print(f"Date Mode Activated")
        self.first_date_time = int(input(f"First DateTime (DD/MM/YYYY) (HH/MM/SS): "))
        self.second_date_time = int(input(f"Second DateTime (DD/MM/YYYY) (HH/MM/SS): "))
        self.calculate()

    def calculate(self):
        self.result = (self.first_date_time - self.second_date_time)
        self.result = self.result.__abs__()


if __name__ == "__main__":
    operators = ["+", "-", "*", "/", "%"]
    main()
