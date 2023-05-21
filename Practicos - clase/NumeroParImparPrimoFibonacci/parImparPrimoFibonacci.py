def paroimpar (numero):
    if numero % 2 == 0:
        print ("El numero es par.")
    else:
        print ("El numero es impar.")

def numeroPrimo (numero):
    cont=0
    for i in range(1,numero+1):
        if numero%i==0:
            cont += 1
    if cont==2:
        print ("Es primo.")
    else:
        print ("No es primo.")
        
def fibonacci (numero):
    val1=0
    val2=1
    cont=0
    for x in range(1,numero+1):
        suma=val1+val2
        if numero==suma:
            cont=cont+1
        val1=val2
        val2=suma
    if cont==1:
        print ("Es Fibonacci.")
    else:
        print ("No es Fibonacci.")
    

numero=int(input("Introduzca un numero para verificar si es par, impar, primo y fibonacci."))


paroimpar(numero)

numeroPrimo(numero)

fibonacci(numero)