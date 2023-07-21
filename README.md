## BINTU APP

This is a small app for quickly retrieving the MAC address of a device. 
The app uses the `https://macvendors.com` API to fetch the required MAC address information. 
Users can use the app in two forms:
+ CMD type: A command-line interface for obtaining MAC addresses.
+ WEB type: A web interface for checking MAC addresses."

## CMD 
In the CMD type, when you run the APP for the first time, it ask you to setup a name for your comapny.<br>

![First time run](./cmd_first.png)

After the up your company name, the APP start for you.

![First time run](./cmd_second.png)

Type in the mac address of the device you want to check.

![First time run](./cmd_third.png)

You can stop or close the APP by typing [x].

![First time run](./cmd_four.png)

# NOTE
Visit Macvendors [macvendors](https://macvendors.com/api) and register for an API.<br>
After registering, you will be provided with your bearer token.<br>
You can then use the APP.<br>

## Installation 
Make sure you have python installed on your device.<br>
Open the cmd_app folder in the terminal and run the bintu.py file `./bintu.py`<br>

### Note that both the cmd and web are all written in pure python.

## WEB
In the web type, you run the APP in the browser, perform some setting by adding your api bearer token, than, you save it.<br>
You then pest your mac address in the search box to see the device the mac address is map too.
