import string

class Calculator:
    def calculate(self):
        while True:
            calculate = input("Gib math: ")
            if all([i in "1234567890+-/*()" for i in calculate]):
                print(eval(calculate))
            else:
                print("Not math?!")

# __name__ predefined variable which is equal to __main__ if this is ran directly in the program.
if __name__ == "__main__":
    calculator = Calculator()
    while True:
        calculator.calculate()
        print("---------------")
