list1 = [int(i) for i in input().split()]
x = int(input())
if x in list1:
    for i in range(len(list1)):
        if list1[i] == x:
            print(i, end=' ')
else:
    print('Отсутствует')