#!/usr/bin/python3
# _*_ coding: utf-8 _*_

alumnes = [{"nom":"Marcel", "cognom_1":"Garcia"}, \
    {"nom":"Marina", "cognom_1":"Cullell"}, \
    {"nom":"Mario",  "cognom_1":"Vizuete"}, \ 
    {"nom":"Antoni", "cognom_1":"Valent"}, \
    {"nom":"Annabel","cognom_1":"Segura"}, \
    {"nom":"Loulou", "cognom_1":"Nadal"} \
]
print("<DOCTYPE html>")
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("<title>Alumnes</title>")
print("<style>")
print("table, th, td {border: 1px solid black;}")
print("</style>")
print("</head>")
print("<body>")
print("<h1>Llistat d'alumnes</h1>")
# A la vida real potser només la part de la taula la escriuria 
# el codi i la resta formaria part d'una plantilla.
print("<table>")
print("<tr>")
print("<th>Nom</th><th>Cognom</th>")
print("</tr>")
for alumne in alumnes:
    print("<tr>")
    print("<td>",alumne["nom"],"</td><td>",alumne["cognom_1"],"</td>")
    print("</tr>")
print("</table>")
print("</body>")