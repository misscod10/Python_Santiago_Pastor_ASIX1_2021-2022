#!/usr/bin/python
import sys
if (len(sys.argv)<3):
    quit()
print(f"nom del programa {sys.argv[0]}")
print(f"resta de paràmetres{sys.argv[1::]}")