import string

class Calculator:
    def calculate(self):
        while True:
            calculate = input("Gib math: ")
            if all([i in "1234567890+-/*()" for i in calculate]):
                print(eval(calculate))
            else:
                print("Not math?!")

# __name__ is equal to "__main__" if the app is run directly
# If instead the code is ran through an import in another program it is going to be equal to the name of the file
if __name__ == "__main__":
    calculator = Calculator()
    while True:
        calculator.calculate()
        print("---------------")
