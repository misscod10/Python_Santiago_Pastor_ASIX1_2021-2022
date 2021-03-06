#!/usr/bin/python3
#_*_ coding: utf-8 _*_

__Author__="Santiago Pastor Serrano"
__Email__="cf19santiago.pastor@iesjoandaustria.org"

"""
Aquest programa agafa el contingut de l'archiu 'plantilla.html', substitueix els camps 'Mtotal''MDISP' i 'MLliure' per els seus valors en /proc/meminfo i escriu un archiu plantilla_final.html amb el contingut canviat.
"""


def main():
    plantilla_lectura=open("plantilla.html","r")
    info=open("/proc/meminfo","r")
    plantilla_final=open("memoria.html","w")
    texto_final=remplazar_caracteres(plantilla_lectura,info)
    plantilla_final.write(texto_final)
    tancar_archius(plantilla_lectura,info,plantilla_final)

    
def tancar_archius(plantilla_lectura,info,plantilla_final):
    plantilla_lectura.close()
    info.close()
    plantilla_final.close()


def remplazar_caracteres(archivo,info):
    texto=archivo.read()
    valors=info.readlines()
    MTotal=limpiar_info(valors[0])
    MDISP=limpiar_info(valors[1])
    MLliure=limpiar_info(valors[2])
    texto=texto.replace("{{MTotal}}",MTotal)
    texto=texto.replace("{{MDisp}}",MDISP)
    texto=texto.replace("{{MLliure}}",MLliure)
    texto_final=texto
    return texto_final


def limpiar_info(info_a_limpiar):
    info_limpia=info_a_limpiar.replace(" ","")
    info_limpia=info_limpia.split(":")
    info_limpia=info_limpia[1]
    return info_limpia 


if __name__=="__main__":
    main()
