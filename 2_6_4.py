ma = []
mb = []
mc = []
while True:
    a = input()
    if a == 'end': break
    ma.append([int(i) for i in a.split()])
for i in range(len(ma)):
    for j in range(len(ma[i])):
        kr = len(ma)
        kc = len(ma[i])
        ma1 = ma[int(((((i - 1) / kr)) - ((i - 1) // kr)) * kr)][j]
        ma2 = ma[int(((((i + 1) / kr)) - ((i + 1) // kr)) * kr)][j]
        ma3 = ma[i][int(((((j - 1) / kc)) - ((j - 1) // kc)) * kc)]
        ma4 = ma[i][int(((((j + 1) / kc)) - ((j + 1) // kc)) * kc)]
        mb.append(ma1 + ma2 + ma3 + ma4)
    mc.append([int(x) for x in mb])
    mb.clear()
for i in range(len(ma)):
    for j in range(len(ma[i])):
        print(mc[i][j], end=' ')
    print()