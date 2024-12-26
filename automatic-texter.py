# Author: guilleacq
# WARNING: This code may work differently in different systems and responses may vary based on PC performance / operating system. 
# I am not responsible for any damage you may cause to your reputation/pc if this works in an unexpected way
# Also, by using this YOU ARE LETTING A PROGRAM MANAGE YOUR COMPUTER and it CANNOT be stopped UNLESS you force stop the process (Ctrl + C). 
# --------------------------------------------------- USE AT YOUR OWN RISK ----------------------------------------------

import pyautogui as pag 
import time

contacts = [
    {"name": "Guillermo Acquistapace", "nickname": "Guillee"},
    {"name": "Notas Personales", "nickname": "Notitas"}
]


def open_whatsapp():
    pag.press("winleft")
    time.sleep(1.5)
    pag.typewrite("WhatsApp")
    time.sleep(1)
    pag.press("enter")
    time.sleep(4)

# Call this function ONLY after open_whatsapp() has been called
def text_contact(contact):
    pag.hotkey("ctrl", "f")
    time.sleep(1)
    pag.hotkey("ctrl", "a")
    pag.press("delete")
    pag.typewrite(contact["name"])
    time.sleep(1)
    pag.press("tab")
    pag.press("enter")
    time.sleep(1)

    # Message logic
    message = "Hola, "+contact["nickname"] # TODO: Esto se va a ir a otra clase
    pag.typewrite(message)
    pag.press("enter")
    time.sleep(1)


def main(): 
    open_whatsapp()

    for contact in contacts:
        text_contact(contact)

if __name__ == "__main__":
    main()