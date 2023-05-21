import math 
import random             
import tkinter as tk

def FuncionSumatoria():
    ecuacion=int(entrada1.get())+int(entrada2.get())+int(entrada3.get())
    resultadoSumatoria["text"]=ecuacion


def FuncionResta():
    ecuacion=int(entrada1.get())-int(entrada2.get())-int(entrada3.get())
    resultadoResta["text"]=ecuacion


def FuncionMultiplicar():
    ecuacion=int(entrada1.get())*int(entrada2.get())*int(entrada3.get())
    resultadoMultiplicar["text"]=ecuacion


def FuncionNumeroMayor():  
    if int(entrada1.get()) >= int(entrada2.get()) and int(entrada1.get()) >= int(entrada3.get()):
        resultadoMayor["text"] = int(entrada1.get())
    else:
        if int(entrada2.get()) >= int(entrada1.get()) and int(entrada2.get()) >= int(entrada3.get()):
            resultadoMayor["text"] = int(entrada2.get())
        else:
            if int(entrada3.get()) >= int(entrada1.get()) and int(entrada3.get()) >= int(entrada2.get()):
                resultadoMayor["text"] = int(entrada3.get())


def FuncionAleatoria():
    numero=random.randint(1,2)
    if numero==1:
        resultado = int(entrada1.get())+int(entrada2.get())+int(entrada3.get())
    else:
        if int(entrada1.get()) >= int(entrada2.get()) and int(entrada1.get()) >= int(entrada3.get()):
            resultado = int(entrada1.get())
        else:
            if int(entrada2.get()) >= int(entrada1.get()) and int(entrada2.get()) >= int(entrada3.get()):
                resultado = int(entrada2.get())
            else:
                if int(entrada3.get()) >= int(entrada1.get()) and int(entrada3.get()) >= int(entrada2.get()):
                    resultado = int(entrada3.get())
    resultadoAleatorio["text"] = resultado
    return resultado

    
def RaizCuadradaAleatorio():
    resultadoAleatorio = FuncionAleatoria()
    raiz_cuadrada = round(math.sqrt(resultadoAleatorio), 2)
    resultadoRaizCuadradaAleatorio["text"] = raiz_cuadrada


def FuncionFormula():
    numeroAleatorio = FuncionAleatoria()
    numeroTexto = str(numeroAleatorio)
    longitudNumero = len(numeroTexto)

    if longitudNumero < 2:
        resultadoFormula["text"] = 0
    elif longitudNumero == 2:
        sacarDigito1 = numeroTexto[0]
        sacarDigito2 = numeroTexto[1]
        digito1 = int(sacarDigito1) ** 2
        digito2 = int(sacarDigito2) * math.pi**2
        resultadoFormula["text"] = digito1 + digito2
    elif longitudNumero == 3:
        sacarDigito3 = numeroTexto[0]
        sacarDigito4 = numeroTexto[1]
        sacarDigito5 = numeroTexto[2]
        digito3 = int(sacarDigito3) ** 2
        digito4 = int(sacarDigito4) ** 2
        digito5 = int(sacarDigito5) * math.pi**2
        resultadoFormula["text"] = digito4 + digito3 + digito5
    elif longitudNumero > 3:
        sacarDigito1 = numeroTexto[0]
        sacarDigito2 = numeroTexto[-1]
        numeroMedios = 1
        for i in range(1, longitudNumero-1):
            sacarDigito8 = numeroTexto[i]
            numeroMedios *= int(sacarDigito8)
        resultadoFormula["text"] = numeroMedios
        
def FuncionSeno():
    numeroAleatorio = FuncionAleatoria()
    numeroTexto = str(numeroAleatorio)
    longitudNumero = len(numeroTexto)

    if longitudNumero < 2:
        ecuacionFinal=0
        resultadoFormula["text"] = 0
    elif longitudNumero == 2:
        sacarDigito1 = numeroTexto[0]
        sacarDigito2 = numeroTexto[1]
        digito1 = int(sacarDigito1) ** 2
        digito2 = int(sacarDigito2) * math.pi**2
        ecuacionFinal=digito1 + digito2
        resultadoFormula["text"] = int(digito1 + digito2)
    elif longitudNumero == 3:
        sacarDigito3 = numeroTexto[0]
        sacarDigito4 = numeroTexto[1]
        sacarDigito5 = numeroTexto[2]
        digito3 = int(sacarDigito3) ** 2
        digito4 = int(sacarDigito4) ** 2
        digito5 = int(sacarDigito5) * math.pi**2
        ecuacionFinal=digito4 + digito3 + digito5
        resultadoFormula["text"] = int(digito4 + digito3 + digito5)
    elif longitudNumero > 3:
        sacarDigito1 = numeroTexto[0]
        sacarDigito2 = numeroTexto[-1]
        numeroMedios = 1
        for i in range(1, longitudNumero-1):
            sacarDigito8 = numeroTexto[i]
            numeroMedios = int(sacarDigito8)
            ecuacionFinal=numeroMedios
        resultadoFormula["text"] = int(numeroMedios)
    
    ecuacionSeno=float(math.sin(ecuacionFinal * math.pi/180))
    resultadoSeno["text"] = ecuacionSeno
    

    

ventana=tk.Tk()
ventana.geometry("500x300")
entrada1=tk.Entry(ventana)
entrada1.grid(row=0,column=0)
entrada2=tk.Entry(ventana)
entrada2.grid(row=0,column=1)
entrada3=tk.Entry(ventana)
entrada3.grid(row=0,column=2)
boton1=tk.Button(ventana,text="Sumatoria", width=9,height=2,command=FuncionSumatoria).grid(row=1,column=0)
boton2=tk.Button(ventana,text="Resta", width=9,height=2,command=FuncionResta).grid(row=1,column=1)
boton3=tk.Button(ventana,text="Multiplicar", width=9,height=2,command=FuncionMultiplicar).grid(row=1,column=2)
boton4=tk.Button(ventana,text="Numero Mayor", width=12,height=2,command=FuncionNumeroMayor).grid(row=3,column=0)
boton5=tk.Button(ventana,text="Aleatorio", width=9,height=2,command=FuncionAleatoria).grid(row=3,column=1)
boton6=tk.Button(ventana,text="Raiz Cuadrada", width=12,height=2,command=RaizCuadradaAleatorio).grid(row=3,column=2)
boton6=tk.Button(ventana,text="Fórmula", width=9,height=2,command=FuncionFormula).grid(row=5,column=0)
boton7=tk.Button(ventana,text="Seno", width=9,height=2,command=FuncionSeno).grid(row=5,column=2)
resultadoSumatoria=tk.Label(ventana)
resultadoSumatoria.grid(row=2, column=0)
resultadoResta=tk.Label(ventana)
resultadoResta.grid(row=2, column=1)
resultadoMultiplicar=tk.Label(ventana)
resultadoMultiplicar.grid(row=2,column=2)
resultadoMayor=tk.Label(ventana)
resultadoMayor.grid(row=4,column=0)
resultadoAleatorio=tk.Label(ventana)
resultadoAleatorio.grid(row=4, column=1)
resultadoRaizCuadradaAleatorio=tk.Label(ventana)
resultadoRaizCuadradaAleatorio.grid(row=4, column=2)
resultadoFormula=tk.Label(ventana)
resultadoFormula.grid(row=6, column=0)
resultadoSeno=tk.Label(ventana)
resultadoSeno.grid(row=6, column=2)
ventana.mainloop()