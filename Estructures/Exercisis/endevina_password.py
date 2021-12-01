#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys, crypt

__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"

"""
Endevina passwords numérics al estil shadow
Mode d'ús:
    time python3 endevina_password.py `openssl passwd -6 -salt UnPessicDeSal 99`
"""


def main(pwd_shadow):
    """
    >>> print(main('$6$bfNlqcskvKPcprPr$B6NH9YTQ1kbFo/xJ09Gi6PFbDE/iorH77qlGC.W/XipUwgH2mMRxsX32wxLUY6xrbm0utU5XzTfnXeHvktaO10'))
    1234
    >>> print(main('$6$UnPessicDeSal$motDspO44FaSqzWRfB7IxzUPMim6xIKYWod8KG4CkKED1ziVSdmZOUAlmNaD9LIcEWodTYMUn.k0NpqT1iZEk.'))
    0099
    """
    camps = pwd_shadow.split('$')
    password = ""
    method = camps[1]
    salt = camps[2]
    pwd_hashed = camps[3]
    comptador = [0,0,0,0]
    while password == "":
        possible_password = crypt.crypt(str(f"{comptador[0]}{comptador[1]}{comptador[2]}{comptador[3]}"), '$' + method + '$' + salt)
        if possible_password == pwd_shadow:
            password = str(comptador[0])+str(comptador[1])+str(comptador[2])+str(comptador[3])
        elif (comptador[0])+1==10:
            comptador[0]=0
            if comptador[1]+1==10:
                comptador[1]=0
                if comptador[2]+1==10:
                    comptador[2]=0
                    comptador[3]= comptador[3]+1
                else:
                    comptador[2]= comptador[2]+1
            else:
                comptador[1]= comptador[1]+1
        else:
            comptador[0]=comptador[0]+1
    return password

if __name__ == "__main__":
    print(main(sys.argv[1]))
