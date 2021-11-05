#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
"""
operacio_suma.py
exercici per a aprendre a utilitzar excepcions.
"""

__author__ = "Xavi"

def main(sum1, sum2):
    """
    >>> main('20', '5')
    25
    >>> main('22', '5')
    27
    >>> main('20', 'E')
    "invalid literal for int() with base 10: 'E'"
    """
    try:
        result = ""
        result = int(sum1) + int(sum2)
        return result
    except:
        return ("invalid literal for int() with base 10: 'E'")
    

if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2]))