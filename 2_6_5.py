n = int(input())
xm = 1
des = 1
n1 = n-1
y = 0
x = 0
a = [[0] * n for i in range(n)]
for j in range(n):
    a[0][j] = xm
    xm += 1
    y = j
for et in range(n + n - 1):
    for i in range(n1):
        x = x + (1 * des)
        a[x][y] = xm
        xm += 1
    des = des * -1
    for j in range(n1):
        y = y + (1 * des)
        a[x][y] = xm
        xm += 1
    n1 -=1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()