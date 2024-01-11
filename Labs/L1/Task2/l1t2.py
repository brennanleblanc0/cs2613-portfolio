import math

def newAbs(x):
    if x < 0:
        return x**-1
    else:
        return x

def f(a, b):
    return math.sqrt(newAbs(((a-1)**5) - newAbs(b + 1)))

progExit = False

while not progExit:
    a = input("Input two values:\n")
    b = input()
    a.split('\n')
    if a == 'X':
        progExit = True
        break
    a = float(a)
    b = float(b)
    print(f"Result: {f(a,b)}")