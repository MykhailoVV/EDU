a = float(input())
b = float(input())
x = input()
if x == '+':
    print(a + b)
elif x == '-':
    print(a - b)
elif x == '*':
    print(a * b)
elif x == 'pow':
    print(a ** b)
elif x == 'mod' or x == 'div' or x == '/':
    if b == 0:
        print('Деление на 0!')
    elif x == 'mod':
        print(a % b)
    elif x == 'div':
        print(a // b)
    elif x == '/':
        print(a / b)
else:
    print('Введены некоректные данные')