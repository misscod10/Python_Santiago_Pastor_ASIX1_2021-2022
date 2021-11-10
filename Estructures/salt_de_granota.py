#!/usr/bin/python3
import sys
import doctest
__author__="Santiago Pastor Serrano"

def main (inici,final,salt):
    if salt == 0:
        raise
    for index in range(inici,final,salt):
        print(index)

if __name__=='__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])