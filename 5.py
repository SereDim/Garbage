''' 3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.Метод рекурсії
Серебренников Дмитрий'''
from random import randint
import numpy as np
import timeit
def A(b, c=0, d=0, c_max=0, d_max=0,maxnum=0):#Функция для проверки элементов
    if d == len(b[c]):
        c += 1  #ряд
        d = 0  #столбец
    if c == len(b):#
        return c_max, d_max#
    if b[c][d] > b[c_max][d_max]:#
        maxnum=b[c][d]#
        c_max = c#
        d_max = d#
    d+=1#
    return A(b, c, d, c_max, d_max)#
n=int (input())#
if 1<=n<=5:#массив
    m=n#
    b=np.zeros((n,m),dtype=int)#
    for c in range(n):#
        for d in range (m):#
            b[c][d]=randint(1,20)
    print(b)#вывод массива
    print(A(b))#выводим индекс макс эелмен
else:
    print('-')#ошибку выводим
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')
'''Написание:год(2часа)
Читабельность плохая
В данном случае рефлексивный способ потребляет больше памяти и код больше чем в итерационном'''
