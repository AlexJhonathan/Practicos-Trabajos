import random
import math
def sumaNumeros(num1,num2,num3):
    sumatoria=num1+num2+num3
    return sumatoria


def numeroMayor3(num1,num2,num3):
    if (num1>num2 and num1>num3):
        numeroMayor=num1
    else:
        if (num2>num1 and num2>num3):
            numeroMayor=num2
        else:
            numeroMayor=num3
    return numeroMayor


def aleatoria(numMayor,suma):
    numRandom=randrange(1,2)
    if numRandom==1:
        numFinal=suma
    else:
        numFinal=numMayor
    return numRandom

def funcionFormula(numeroElegidoAlAzar,numeroTexto,longitudNumero ):
    if longitudNumero==2:
        primerNumeroTexto=(numeroTexto[0])
        primerNumero=int(primerNumeroTexto)
        ultimoNumeroTexto=(numeroTexto[-1])
        ultimoNumero=int(ultimoNumeroTexto)
        potenciaPrimera=(primerNumero**2)
        piUltimo=(ultimoNumero*math.pi)
        return (potenciaPrimera+piUltimo)
    else:
        if longitudNumero==3:
            primerNumeroTexto=(numeroTexto[0])
            primerNumero=int(primerNumeroTexto)
            ultimoNumeroTexto=(numeroTexto[-1])
            ultimoNumero=int(ultimoNumeroTexto)
            numeroCentralTexto=(numeroTexto[1])
            numeroCentral=int(numeroCentralTexto)
            potenciaPrimera=(primerNumero**2)
            piUltimo=(ultimoNumero*math.pi)
            return (potenciaPrimera+piUltimo+numeroCentral)
        else:
            if longitudNumero>3:
                primerNumeroTexto=(numeroTexto[0])
                primerNumero=int(primerNumeroTexto)
                ultimoNumeroTexto=(numeroTexto[-1])
                ultimoNumero=int(ultimoNumeroTexto)
                potenciaPrimera=(primerNumero**2)
                piUltimo=(ultimoNumero*math.pi)
                B=1
                nCentroFinal=1
                while B<=(longitudNumero-2):
                    nCentralTexto=(numeroTexto[B])
                    nCentroNumeral=int(nCentralTexto)
                    nCentroFinal=(nCentroFinal*nCentroNumeral)
                    B=B+1
                return potenciaPrimera+piUltimo+nCentroFinal
            else:
                return numeroElegidoAlAzar
                

def RaizCuadrada ( numerofinal):
  RaizCuadrada = math.sqrt( numerofinal)
  
def seno (numerofinal):
    return math.sin(numerofinal)


print("Introduzca tres numeros.")
num1=int(input())
num2=int(input())
num3=int(input())
numMayor=numeroMayor3(num1,num2,num3)
suma=sumaNumeros(num1,num2,num3)
numAle=aleatoria(numMayor,suma)
numerofinal=FuncionFormula(numeroElegidoAlAzar,numeroAlAzar,numeroTexto,longitudNumero )
print("EL resultado de la sumatoria es: ",suma)
print("El número mayor es: ",numMayor)
print("El resultado de la fórmula es: ",funcionFormula(numeroElegidoAlAzar,numeroTexto,longitudNumero ))
print("EL resultado de la raiz es: ",RaizCuadrada(numerofinal))
print("En funcion de seno es: ",seno(numerofinal))


