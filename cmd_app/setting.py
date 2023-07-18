import os

path="bintu\cmd_app\menu.txt"

def setting_write(text):
    """
        This function allows the user to customize
        the app by writing the name of user compay to file
    """
    with open(path,"a") as file:
        text+="\n"
        output = file.write(text)
        return output
    
def setting_read():
    """
        This function reads the name of the company from fle
    """
    with open(path,"r") as file:
        return file.read().splitlines()
    

def main():
    motd = "WELCOME TO THE BINTU MAC FINDER\n "
    if os.path.exists(path) == False:
        output = input(f"{motd}Enter the name of your Company:> ")
        setting_write(output)
        bearer = input("Enter Bearer token:> ")
        setting_write(bearer)
    if os.stat(path).st_size == 0:
        pass
    else:
        ot = setting_read()
        NAME = ot[0].upper()
        BEARER = ot[1]
        return NAME,BEARER

