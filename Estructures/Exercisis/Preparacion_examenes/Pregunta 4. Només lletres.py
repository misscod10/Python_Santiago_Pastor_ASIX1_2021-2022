#!/usr/bin/python3
# _*_ coding: utf-8 _*_
print("Text?")
text = input()
cadena=""
for i in text:
    if i.isalpha() == True:
        cadena = cadena + i
print(cadena)