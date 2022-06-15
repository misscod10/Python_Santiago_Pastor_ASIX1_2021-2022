#!/usr/bin/python3
# _*_ coding: utf-8 _*_

__author__="Santiago Pastor Serrano"
__email__="cf19santiago.pastor@iesjoandaustria.org"

import json, requests

"""
Aquest programa envia un missatge al server de discord quan detecta que l'equip utilitza més de la meitat de ram disponible.
He reutilitzat tant la part del codi que envia el missatge a Discord com la part que agafa la memoria del /proc/meminfo de altres codis
que he fet anteriorment.
"""


def main():
    info=open("/proc/meminfo","r")
    valors=info.readlines()
    mem_total=limpiar_info(valors[0])
    mem_libre=limpiar_info(valors[1])
    if (mem_libre/mem_total)<0.5:
        enviar_mensaje()


def limpiar_info(info_a_limpiar):
    info_limpia=info_a_limpiar.replace(" ","").replace("kB","")
    info_limpia=info_limpia.split(":")
    info_limpia=info_limpia[1]
    info_limpia=int(info_limpia)
    return info_limpia 


def enviar_mensaje():
    webhook="https://discord.com/api/webhooks/953582781466832907/7JvJXtGMmPOvz1M1nWa2pXU2hUuYbb06nuviGqYE3smsF-I3KdDXDC3m3Qpy6cJ4y8Vi"
    headers={"Content-Type":"application/json"}
    missatge=json.dumps({"content":"Compte!!, la ram utilitzada supera el 50% de la ram total."})
    requests.post(webhook, data=missatge , headers=headers)


if __name__=="__main__":
    main()