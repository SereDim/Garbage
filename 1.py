'''1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n через рекурсію
Серебренников Дмитрий'''
import timeit
def b(a):
    if a==0:
        return 1
    else:
        return b(a-1)*a #через саму себя
c=int(input())
print(b(c))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')

'''Написание:5мин
Читабельность:удовлетворительная'''
