#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int (input('введите число N: '))

stop = 0
p = 2
for i in range(N):
    if stop != 1:
        p = p ** i
        if p <= N:
            print(p, end=' ')
            p = 2
        else:
            stop = 1
    else:
        i = N