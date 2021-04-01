st = []
a = int(input())
for i in range(1 , a + 1):
    st += [i] * i
for i in range(a):
    print(st[i], end=' ')