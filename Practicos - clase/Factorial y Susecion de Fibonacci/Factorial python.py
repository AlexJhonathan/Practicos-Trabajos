num = int(input("Introduzca un numero positivo para calcular su factorial: "))

while num < 0:
    print("ERROR: Solo numeros positivos.")
    num = int(input("Introduzca un numero positivo para calcular su factorial: "))

factorial = 1
desarrollo = ""

if num == 0:
    print("El factorial de 0 es: 1")
else:
    for x in range(int(num), 0, -1):
        factorial = factorial * x
        if x > 1:
            desarrollo = desarrollo + str(x) + "x"
        else:
            desarrollo = desarrollo + str(x)
    print("El factorial de", num, "es:", desarrollo, "=", factorial)