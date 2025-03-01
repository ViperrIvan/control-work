from math import factorial
def combinations(n1, m1):
    res = factorial(n1) / (factorial(n1 - m1)*factorial(m1))
    return int(res)
print("****** СОЧЕТАНИЯ ******")
n = int(input("Введи кол-во объектов: "))
m = int(input("Введи по сколько их разместить: "))
print(combinations(n, m))
