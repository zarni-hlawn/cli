# This is the cli version of the "Project 0 Calculator"


def main():
    app = Calculator()


class Calculator:
    def __init__(self):
        print("Calculator Is Now Running Successfully ~")
        while True:
            try:
                self.choice = float(input("1. Simple 2. Scientific 3. Date  !Default is 'Simple'"))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if self.choice == 1:
            self.simple = Simple()
        if self.choice == 2:
            self.scientific = Scientific()
        if self.choice == 3:
            self.date = Date()


class Simple:
    def __init__(self):
        print("Simple Mode Activated")


class Scientific:
    def __init__(self):
        print("Scientific Mode Activated")


class Date:
    def __init__(self):
        print("Date Mode Activated")


main()
