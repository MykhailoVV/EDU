x = input()
if x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    print((p * (p - a)*(p - b)*(p - c)) ** 0.5)
elif x == 'круг':
    a = int(input())
    print(3.14 * a ** 2)
elif x == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
else:
    print('Что то пошло не так')