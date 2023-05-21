def totalAntiguedad(añosAntiguedad):
 if añosAntiguedad<2:
     return 0
 else:
     if añosAntiguedad>=5 and añosAntiguedad<8:
         return 11/100 * 2250 * 3
     else:
         if añosAntiguedad>=8 and añosAntiguedad<11:
             return 11/100 * 2250 * 3
         else:
             if añosAntiguedad>=8 and añosAntiguedad<11:
                 return 18/100 * 2250 * 3
             else:
                 if añosAntiguedad>=11 and añosAntiguedad<15:
                    return 26/100 * 2250 * 3
                 else:
                     if añosAntiguedad>=15 and añosAntiguedad<20:
                         return 34/100 * 2250 * 3
                     else:
                         if añosAntiguedad>=20 and añosAntiguedad<25:
                             return 42/100 * 2250 * 3
                         else:
                             if añosAntiguedad>=25:
                                 return 50/100 * 2250 * 3
                             else:
                                 return 0

def valorNacional(sueldo):
    if sueldo < 13000:
        return sueldo*0.005
    else:
        if sueldo < 25000:
            return (sueldo-13000)*(1/100)
        else:
            if sueldo < 35000:
                return (sueldo - 25000)*(3/100)
            else:
                if sueldo > 35000:
                    return (sueldo - 35000)*(5/100)
                else:
                    return 0
       
def pagosHorasEx(condicionHorasExtras, numHorasExtras, sueldo, numHorasTrabajadas):
    if condicionHorasExtras == 1:
        pagoHorasExtras = numHorasExtras * (sueldo / numHorasTrabajadas)
        print("Tu bono por horas extras es de", pagoHorasExtras)
    elif condicionHorasExtras == 2:
        pagoHorasExtras = numHorasExtras * (sueldo / numHorasTrabajadas) * 1.25
        print("Tu bono por horas extras es de", pagoHorasExtras)
    elif condicionHorasExtras == 3:
        pagoHorasExtras = numHorasExtras * (sueldo / numHorasTrabajadas) * 2
        print("Tu bono por horas extras es de", pagoHorasExtras)
    else:
        pagoHorasExtras = 0
    return pagoHorasExtras
    

nombre=input("Introduzca su nombre completo.")
ci=int(input("Introduzca su carnet de Identidad."))
cargo=input("¿Cual es su cargo?")
añoActual=int(input("Introduzca el año actual."))
sueldo=int(input("Introduzca su sueldo mensual."))
añoIngreso=int(input("Indique el año en el que ingresó a la empresa."))

añosAntiguedad=añoActual-añoIngreso

valorAntiguedad=totalAntiguedad(añosAntiguedad)

print("Su bono por antiguedad es de: ",valorAntiguedad)

aporteNacional=valorNacional(sueldo)

print("Su aporte nacional es de ",aporteNacional)

numHorasTrabajadas=int(input("¿Cuantas horas a trabajado en todo el mes sin tener en cuenta las horas extras?"))

horasExtras=input("¿Trabajo horas extra?")

if horasExtras=="si":
    numHorasExtras=int(input("¿Cuántas horas extras trabajó?"))
    condicionHorasExtras=int(input("En qué condiciones fueron esas horas extras, 1: diurno  2: nocturno  3: feriados"))
    
else:
    print ("Tu bono por horas extras es de ",0)
    
totalGanado=int(sueldo+valorAntiguedad+pagosHorasEx(condicionHorasExtras,numHorasExtras,sueldo,numHorasTrabajadas))
print("Su total Ganado es ", totalGanado)

anticipo=input("¿Le otorgaron algun anticipo?")
if anticipo=="si":
    cantAnticipos=int(input("¿Que cantidad le anticiparon?"))
else:
    cantAnticipos=int(0)
    
afp=(12.71/100)*totalGanado
totalEgresos=round(afp+cantAnticipos+valorNacional(sueldo))
print("Sus egresos totales son de ",totalEgresos)

liquidoPagable=round(totalGanado-totalEgresos)

print(nombre + " con cargo " + cargo + " y carnet de identidad " + str(ci) + ", su liquido pagable es de " + str(liquidoPagable) + " bs.")
    
    


