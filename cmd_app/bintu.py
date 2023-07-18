#!/usr/bin/python3

import requests
import os
from time import sleep
from setting import main

welcom_txt = main()[0]
endpoint = "https://api.macvendors.com/v1/lookup"
bearer = main()[1]
logo =f"""
            WELCOME TO {welcom_txt} MAC ADDRESS FINDER
                ( type [x] to abort )
"""

keys = True
while keys:
    print(logo) 

    mac_address = input("Please enter mac address: ")
    headers = {
        "Authorization": bearer
    }

    response = requests.get(url=f"{endpoint}/{mac_address}", headers=headers)
    address_find = response.json()

    def run():
        try:
            print(f"DEVICE NAME: {address_find['data']['organization_name']}".upper())
        except:
            print("Please enter a valid mac address")

    if mac_address == "x".lower():
        keys = False

    run()
    sleep(10)
    os.system("clear")
