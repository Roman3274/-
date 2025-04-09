class Calculator:
    def __init__(self, a, b):
        if not str(a).isdigit() or not str(b).isdigit():
            raise TypeError("a та b мають бути числами (цілі додатні).")
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return self.a / self.b


while True:
    num1 = input("num1 = ")
    num2 = input("num2 = ")
    operation = input("operation (+, -, *, /) або 0 для виходу: ")

    if operation == "0":
        print("Завершення програми.")
        break

    try:
        calc = Calculator(num1, num2)

        if operation == "+":
            print("Результат:", calc.add())
        elif operation == "-":
            print("Результат:", calc.subtract())
        elif operation == "*":
            print("Результат:", calc.multiply())
        elif operation == "/":
            print("Результат:", calc.divide())
        else:
            print("Невірна операція!")

    except TypeError as e:
        print("Помилка типу:", e)
    except ZeroDivisionError as e:
        print("Помилка ділення:", e)

