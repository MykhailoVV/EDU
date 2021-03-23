x = int(input())
dx = 0
sx = 0
if 0 <= x <= 1000:
    sx = x // 100
    dx = ( x - sx * 100) // 10
    ex = x - sx * 100 - dx * 10
    if dx ==1:
        xs = 'ов'
    else:
        if ex in (0, 5, 6, 7, 8, 9):
            xs = 'ов'
        elif ex == 1:
            xs = ''
        elif ex in (2, 3, 4):
            xs = 'а'
else:
    print('Что то пошло не так')
es = str(x) + ' программист' + xs
print(es)