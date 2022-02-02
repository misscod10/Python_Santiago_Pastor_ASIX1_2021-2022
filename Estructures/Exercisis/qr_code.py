#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import qrcode
"""
Un programa que crea un codi qr
"""
__author__   = "Santiago Pastor Serrano"
__email__    = "cf19santiago.pastor@iesjoandaustria.org"
__license__  = "GPL V3"
data='Amobus'
path= './qrs/qr.png'
img = qrcode.make(data)
img.save(path)