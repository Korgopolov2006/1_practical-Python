
import math

#Ето сложения
def addition(a, b):
    return a + b

#Ито вычитания
def subtraction(a, b):
    return a - b

#Вот это вот умножении
def multiplication(a, b):
    return a * b

#А вот это  делению
def division(a, b):
    if b == 0:
        return "Деление на ноль нельзя."
    else:
        return a / b

#эта штука возведения в степень
def exponentiation(a, b):
    return a ** b

# Вот тут искать квадратный корень
def square_root(a):
    if a < 0:
        return "Квадратный корень из отрицательного числа нельзя найти."
    else:
        return math.sqrt(a)

# Тут искать факториал числа
def factorial(a):
    if a < 0:
        return "Факториал отрицательного числа не определен."
    elif a == 0:
        return 1
    else:
        return math.factorial(a)

#  синус
def sine(a):
    return math.sin(a)

#  косинус
def cosine(a):
    return math.cos(a)

#  тангенс
def tangent(a):
    return math.tan(a)

# Проверять ввод чисел
def check_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Пожалуйста, введите число, с которым мы будем работать")

# Проверять ввод символов
def check_symbol_input(prompt):
    while True:
        symbol = input(prompt)
        if len(symbol) == 1:
            return symbol
        else:
            print("Пожалуйста, введите только один символ.")

# проверять ввода операции
def check_operation_input(prompt):
    operations = ["+", "-", "*", "/", "^", "sqrt", "!", "sin", "cos", "tan"]
    while True:
        operation = input(prompt)
        if operation in operations:
            return operation
        else:
            print("Пожалуйста, введите допустимую операцию, указанной вами операции нет")

# Это база
def calculator():
    print("Ынженерный калькулятор")
    a = check_number_input("Введите  число , с которым хотите совершать манипуляции ")
    operation = check_operation_input("Введите операцию (+, -, *, /, ^, sqrt, !, sin, cos, tan): ")

    if operation in ["sqrt", "!", "sin", "cos", "tan"]:
        if operation == "sqrt":
            result = square_root(a)
        elif operation == "!":
            result = factorial(a)
        elif operation == "sin":
            result = sine(a)
        elif operation == "cos":
            result = cosine(a)
        elif operation == "tan":
            result = tangent(a)
            
        print(f"Результат: {result}")
    else:
        b = check_number_input("Введите второе число: ")

        if operation == "+":
            result = addition(a, b)
        elif operation == "-":
            result = subtraction(a, b)
        elif operation == "*":
            result = multiplication(a, b)
        elif operation == "/":
            result = division(a, b)
        elif operation == "^":
            result = exponentiation(a, b)

        print(f"Результат: {result}")


calculator()

