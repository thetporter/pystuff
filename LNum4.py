import random
import math

print("Welcome to Calculator!")
while True:
    print("Enter\n+ for X+Y\t  - for X-Y\n* for X*Y\t  / for X/Y\n^ for X^Y\t  | for |X|\nR for Random\t  ! for X!\nC for arccos(X)\t  Q to quit")
    # Получение операции для выполнения:
    op = input()
    match op:
        case "+":
            # Сложение
            print("Enter X: ", end='')
            x = float(input())
            print("Enter Y: ", end='')
            y = float(input())
            print(str(x) + op + str(y) + " = " + str(x+y))
        case "-":
            # Вычитание
            print("Enter X: ", end='')
            x = float(input())
            print("Enter Y: ", end='')
            y = float(input())
            print(str(x) + op + str(y) + " = " + str(x-y))
        case "/":
            # Деление
            print("Enter X: ", end='')
            x = float(input())
            print("\nEnter Y: ", end='')
            y = float(input())
            print(str(x) + op + str(y) + " = " + str(x/y))
        case "*":
            # Умножение
            print("Enter X: ", end='')
            x = float(input())
            print("Enter Y: ", end='')
            y = float(input())
            print(str(x) + op + str(y) + " = " + str(x*y))
        case "^":
        # Возведение в степень
            print("Enter X: ", end='')
            x = float(input())
            print("Enter Y: ", end='')
            y = float(input())
            i = 1
            res = x
            while i < y:
                res *= x
            print(str(x) + op + str(y) + " = " + str(res))
        case "|":
            # Модуль
            print("Enter X: ", end='')
            x = float(input())
            print("|" + str(x) + "| = " + str(abs(x)))
        case "R":
            # Случайное число от х до у:
            print("Enter lower limit: ", end='')
            x = float(input())
            print("Enter upper limit: ", end='')
            y = float(input())
            print("Random in range (" + str(x) + "; " + str(y) + ") = " + str(random.random() * (y-x) + x))
        case "!":
            # Факториал
            print("Enter X: ", end='')
            x = int(input())
            i = 1
            j = 1
            if x > 0:
                while i <= x:
                   j *= i
                   i += 1
            else: 
                i -= 2
                while i >= x:
                   j *= i
                   i -= 1
            print(str(x) + "! = " + str(j))
        case "C":
            # Арккосинус, углы в радианах:
            print("Enter angle (rad): ", end='')
            x = float(input())
            res = math.acos(x)
            print("acos(" + str(x) + ") = " + str(res))
        case "Q":
            break
        case default:
            # В случае другого ввода:
            print("Invalid input!")
print("Calculator is closing...")