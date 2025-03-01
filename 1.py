from math import factorial
def placement(n1, m1):
    res = factorial(n1) / factorial(n1 - m1)
    return int(res)
print("****** РАЗМЕЩЕНИЯ ******")
n = int(input("Введи кол-во объектов: "))
m = int(input("Введи по сколько их разместить: "))
print(placement(n, m))
