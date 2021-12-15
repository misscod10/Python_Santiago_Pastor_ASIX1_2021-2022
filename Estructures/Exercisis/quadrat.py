#!/usr/bin/python3
# _*_ coding: utf-8 _*_
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
import sys
def main(n):
    for y in range(n):
        for i in range(n+1):
            columnas=("")
            for x in range(n+1):
                columnas= columnas + " " + str(x)
            print(columnas)
        print((" "+"-")*(n+1))
if __name__=='__main__':
    main(int(sys.argv[1]))