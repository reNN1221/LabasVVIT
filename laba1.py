try:
    a = int(input())
    for i in range(a):
        print(i + 1)
except ValueError:
    print("Некорректные данные")
try:
    b = int(input())
    c = int(input())
    if b > c:
        print(b)
    elif b < c:
        print(c)
    else:
        print('=')
except ValueError:
    print("Некорректные данные")
