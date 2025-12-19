import package.module1 as m1
import package.module2 as m2
try:

    a = int(input())
    b = int(input())
    print(m1.multiplication(a, b))
except ValueError:
    print("Please enter an integer")

try:
    c = str(input())
    d = int(input())
    print(m2.string(c, d))
except ValueError:
    print("Please enter an integer or string")
except IndexError:
    print("Please enter an string")