#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
Aquest programa ens permet crear una calculadora visual i sumar digits.
"""

__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

import tkinter
valor_en_pantalla = 0
valor_acumulado = 0
operacio=""
def click_boto_digit(digit):
    global valor_en_pantalla
    valor_en_pantalla *= 10
    valor_en_pantalla +=  digit

    entrada.delete(0, tkinter.END)
    entrada.insert(0, f"{valor_en_pantalla}")

def vaciar():
    global valor_en_pantalla, valor_acumulado
    entrada.delete(0, tkinter.END)
    entrada.insert(0, 0)
    valor_en_pantalla=0
    valor_acumulado=0
    
def icono_sumar():
    global valor_en_pantalla, valor_acumulado, operacio
    valor_acumulado=valor_en_pantalla
    valor_en_pantalla=0
    operacio="+"
    
def icono_restar():
    global valor_en_pantalla, valor_acumulado, operacio
    valor_acumulado=valor_en_pantalla
    valor_en_pantalla=0
    operacio="-"

def icono_multiplicar():
    global valor_en_pantalla, valor_acumulado, operacio
    valor_acumulado=valor_en_pantalla
    valor_en_pantalla=0
    operacio="*"

def icono_dividir():
    global valor_en_pantalla, valor_acumulado, operacio
    valor_acumulado=valor_en_pantalla
    valor_en_pantalla=0
    operacio="/"

def icono_igual():
    global valor_en_pantalla, valor_acumulado, operacio
    if operacio=="+":
        valor_en_pantalla=valor_en_pantalla+valor_acumulado
    elif operacio=="-":
        valor_en_pantalla=valor_acumulado-valor_en_pantalla
    elif operacio=="/":
        valor_en_pantalla=valor_acumulado/valor_en_pantalla
    elif operacio=="*":
        valor_en_pantalla=valor_en_pantalla*valor_acumulado
    entrada.delete(0, tkinter.END)
    entrada.insert(0, f"{valor_en_pantalla}")

finestra = tkinter.Tk()

entrada = tkinter.Entry(finestra, width=50)
entrada.grid(row=0,column=0, columnspan=4)
entrada.insert(0, "0")

boto_01 = tkinter.Button(finestra, 
                    text="1", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(1))
boto_02 = tkinter.Button(finestra, 
                    text="2", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(2))
boto_03 = tkinter.Button(finestra, 
                    text="3", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(3))
boto_04 = tkinter.Button(finestra, 
                    text="4", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(4))
boto_05 = tkinter.Button(finestra, 
                    text="5", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(5))
boto_06 = tkinter.Button(finestra, 
                    text="6", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(6))
boto_07 = tkinter.Button(finestra, 
                    text="7", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(7))
boto_08 = tkinter.Button(finestra, 
                    text="8", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(8))
boto_09 = tkinter.Button(finestra, 
                    text="9", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(9))       
boto_00 = tkinter.Button(finestra, 
                    text="0", 
                    padx=50, 
                    pady=50,
                    command=lambda : click_boto_digit(0))
boto_suma = tkinter.Button(finestra, 
                    text="+", 
                    padx=50, 
                    pady=50,
                    command=lambda : icono_sumar())
boto_resta = tkinter.Button(finestra, 
                    text="-", 
                    padx=50, 
                    pady=50,
                    command=lambda : icono_restar())
boto_multiplicacio = tkinter.Button(finestra, 
                    text="*", 
                    padx=50, 
                    pady=50,
                    command=lambda : icono_multiplicar())
boto_divisio = tkinter.Button(finestra, 
                    text="/", 
                    padx=50, 
                    pady=50,
                    command=lambda : icono_dividir())
boto_igual = tkinter.Button(finestra, 
                    text="=", 
                    padx=50, 
                    pady=50,
                    command=lambda : icono_igual())
boto_vaciar = tkinter.Button(finestra,
                    text="C",
                    padx=50,
                    pady=50,
                    command=lambda : vaciar())
             
boto_01.grid(row=1, column=0)
boto_02.grid(row=1, column=1)
boto_03.grid(row=1, column=2)

boto_04.grid(row=2, column=0)
boto_05.grid(row=2, column=1)
boto_06.grid(row=2, column=2)

boto_07.grid(row=3, column=0)
boto_08.grid(row=3, column=1)
boto_09.grid(row=3, column=2)

boto_00.grid(row=4, column=0)
boto_suma.grid(row=4, column=1)
boto_resta.grid(row=4, column=2)

boto_multiplicacio.grid(row=5, column=0)
boto_divisio.grid(row=5, column=1)
boto_igual.grid(row=5, column=2)

boto_vaciar.grid(row=6, column=0)

finestra.mainloop()