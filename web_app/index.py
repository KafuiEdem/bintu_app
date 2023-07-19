#!/usr/bin/python3

import requests
from cmd_app.setting import main


endpoint = "https://api.macvendors.com/v1/lookup"

#setting up all the elements
company_name = Element("company")

name = main()[0]
bearer = main()[1]
company_name.write(name)

mac_address = input("Please enter mac address: ")
headers = {
        "Authorization": bearer
    }
response = requests.get(url=f"{endpoint}/{mac_address}", headers=headers)
address_find = response.json()

def run():
    try:
        return f"DEVICE NAME: {address_find['data']['organization_name']}".upper()
    except:
        return "Please enter a valid mac address"

def data():
    pass   


def main(*a,**ab):
    pass