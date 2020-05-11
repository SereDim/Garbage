''' 3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.Метод ітерації
Серебренников Дмитрий'''
from random import randint
import numpy as np
import timeit
def A(b):#созд функ для проверки элем
    cmax = 0
    dmax = 0#
    maX=0#макс элем
    for c in range(len(b)):#
        for d in range(len(b)):#
            if b[c][d] > b[cmax][dmax]:#
                maX=b[c][d]#
                cmax=c#
                dmax=d#
    return (f'Max:{maX} on {cmax+1},{dmax+1}')#
n=int(input())#
if 1<=n<=5:#Создание массива
    m=n#
    a=np.zeros((n,m),dtype=int)#
    for h in range(n):#
        for q in range(m):#
            a[h][q]=randint(1,20)#диапазон от 1 к 20
    print(a)#
    print(A(a))#
else:#
    print('-')#слишком большое число
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')
'''Прще чем прошлый, заняло 30 мин
Потребляет меньше памяти'''
