num = int(input("Introduzca la cantidad de numeros que desea generar de la sucesion de Fibonacci: "))
x = 1
m = 0
n = 1

while x <= num:
    if x % 2 == 1:
        print(m)
        m = m + n
    else:
        print(n)
        n = n + m
    x = x + 1