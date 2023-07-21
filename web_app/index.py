import requests
import pyodide_http

# endpoint = "https://api.macvendors.com/v1/lookup"

# # #setting up all the elements
# # company_name = Element("company")
# mac_address = Element("mac")
# show_mac = Element("show-mac")


# company_name.write(name)




# def run():
bearer = ""

#     # mac_address = input("Please enter mac address: ")
#     headers = {
#             "Authorization": bearer
#     }

#     pyodide_http.patch_all()
#     response = requests.get(url=f"{endpoint}/{mac_address.value}", headers=headers)
#     address_find = response.json()
#     try:
#         show_mac.write(f"DEVICE NAME: {address_find['data']['organization_name']}".upper())
#         # return
#     except:
#         show_mac.write("Please enter a valid mac address")
#         # return "Please enter a valid mac address"

# def data():
#     pass   


# def main(*a,**ab):
#     run()




# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()

        # Make a request to the JSON Placeholder API
# response = requests.get("https://api.macvendors.com/v1/lookup/000142")
mac_address="000142"
headers = {
        
        "Authorization": bearer,
        "accept": "application/json",
        "Access-Control-Allow-Origin":"*"
    }
endpoint = "https://api.macvendors.com/v1/lookup"
response = requests.get(url=f"{endpoint}/{mac_address}", headers=headers)
print(response.json())