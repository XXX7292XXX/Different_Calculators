# -*- coding: windows-1251 -*-
# Выводим список доступных операций
class Calculator():
    def Easy_Calculator(self):
        expression = input("Enter an expression: ")
        result = eval(expression)
        print("Result:", result)
    def Mid_Calculator(self):
        print("Available operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Choose an operation (enter the corresponding number): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "1":
            result = num1 + num2
            print("Result:", result)
        elif operation == "2":
            result = num1 - num2
            print("Result:", result)
        elif operation == "3":
           result = num1 * num2
           print("Result:", result)
        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print("Result:", result)
            else:
                print("Error: Division by zero is not possible!")
        else:
            print("Error: Invalid operation!")

    def Hard_Calculator(self):
        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            if y != 0:
                return x / y
            else:
                return "Error: Division by zero!"

        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter the operation number (1/2/3/4): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid input for operation!")

print("Choose the calculator difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter the operation number (1/2/3): ")
call = Calculator()
if choice == '1':
    res = call.Easy_Calculator()
elif choice == '2':
    res = call.Mid_Calculator()
elif choice == '3':
    res = call.Hard_Calculator()