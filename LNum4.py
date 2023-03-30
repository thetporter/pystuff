import random
import math

print("Enter\n+ for X+Y\n- for X-Y\n* for X*Y\n/ for X/Y\n^ for X^Y\n| for |X|\nR for Random\n! for X!\nC for arccos(X)")
op = input()
match op:
    case "+":
        print("Enter X: ", end='')
        x = float(input())
        print("Enter Y: ", end='')
        y = float(input())
        print(str(x) + op + str(y) + " = " + str(x+y))
    case "-":
        print("Enter X: ", end='')
        x = float(input())
        print("Enter Y: ", end='')
        y = float(input())
        print(str(x) + op + str(y) + " = " + str(x-y))
    case "/":
        print("Enter X: ", end='')
        x = float(input())
        print("\nEnter Y: ", end='')
        y = float(input())
        print(str(x) + op + str(y) + " = " + str(x/y))
    case "*":
        print("Enter X: ", end='')
        x = float(input())
        print("Enter Y: ", end='')
        y = float(input())
        print(str(x) + op + str(y) + " = " + str(x*y))
    case "^":
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
        print("Enter X: ", end='')
        x = float(input())
        print("|" + str(x) + "| = " + str(abs(x)))
    case "R":
        print("Enter lower limit: ", end='')
        x = float(input())
        print("Enter upper limit: ", end='')
        y = float(input())
        print("Random in range (" + str(x) + "; " + str(y) + ") = " + str(random.random() * (y-x) + x))
    case "!":
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
        print("Enter angle (rad): ", end='')
        x = float(input())
        res = math.acos(x)
        print("acos(" + str(x) + ") = " + str(res))
    case default:
        print("Invalid input")