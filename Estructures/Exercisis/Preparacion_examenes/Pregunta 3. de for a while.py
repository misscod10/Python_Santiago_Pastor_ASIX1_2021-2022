
#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""
Aquest programa suma números repasant els números del 1 al 100 en salts de 3 i pregunta per cadascuns d'aquests a l'usuari. Si diu que si els afegeix a la suma.
"""
suma=0
valor=1
while valor != 100:
    print("Vols el ", str(valor)," ?")
    resposta=input()
    if resposta == "si" or resposta == "s":
        suma= suma + valor
    valor = valor + 3
print(suma)
