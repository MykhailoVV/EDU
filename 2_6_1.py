s = 0
q = 0
while 1:
    i = int(input())
    s += i
    q = q + (i * i)
    if s == 0:
        print(q)
        break
