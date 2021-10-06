#!/usr/bin/python
# Exercisi 1
lista=[]
cuenta=0
suma_total=0
while True:
    nombre_natural= int(input("Ingresa un número natural: "))
    if nombre_natural== 0:
        break
    else:
        nombre_natural.append(nombre_natural)
        cuenta=+1
print(lista)
for i in lista():
    suma_total=+i
print("El valor mitg és: ", (suma_total/cuenta))
