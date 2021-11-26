#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
for i in range(1,111):
    if i%3 == 0:
        if i%5 == 0:
            print("BlassTizz")
            if i%7 == 0:
                print("BlassTizzZaff")
        elif i%7 == 0:
            print("BlassZaff")
        else:
            print("Blass")        
    elif i%5 == 0:
        if i%7 == 0:
            print("TizzZaff")
        else:
            print("Tizz")
    elif i%7 == 0:
        print("Zaff")
    else:
        print(i)