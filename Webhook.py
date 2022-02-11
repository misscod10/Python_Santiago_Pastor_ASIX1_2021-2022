#!/usr/bin/python3
# _*_ coding: utf-8 _*_
from email import header
import requests
import sys
import json
webhook="https://discordapp.com/api/webhooks/941717401643409458/ruDhevUFmhG3O5zw3RxTgZV3AjH92lQQfAfHrSYm-Y1IYDJx956zjA7D_MMue_HzBYJ-"
headers={"Content-Type":"application/json"}
missatge=json.dumps({"content":sys.argv[1]})
requests.post(webhook, data=missatge , headers=headers)