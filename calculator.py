import string

class Calculator:
    def calculate(self):
        while True:
            calculate = input("Gib math: ")
            if all([i in "1234567890+-/*()" for i in calculate]):
                print(eval(calculate))
            else:
                print("Not math?!")

if __name__ == "__main__":
    calculator = Calculator()
    while True:
        calculator.calculate()
        print("---------------")