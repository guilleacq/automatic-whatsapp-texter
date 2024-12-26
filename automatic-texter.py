# Author: guilleacq
# WARNING: This code may work differently in different systems and responses may vary based on PC performance / operating system. 
# I am not responsible for any damage you may cause to your reputation/pc if this works in an unexpected way
# Also, by using this YOU ARE LETTING A PROGRAM MANAGE YOUR COMPUTER and it CANNOT be stopped UNLESS you force stop the process (Ctrl + C). 
# --------------------------------------------------- USE AT YOUR OWN RISK ----------------------------------------------

import pyautogui as pag 
import time

contacts = ["Guillermo Acquistapace", "Notas Personales"]
contact_nicknames = ["yop", "guille"]

def open_whatsapp():
    pag.press("winleft")
    time.sleep(1.5)
    pag.typewrite("WhatsApp")
    time.sleep(1)
    pag.press("enter")
    time.sleep(4)

# Call this function ONLY after open_whatsapp() has been called
def text_contact(contact_name, contact_nickname):
    pag.hotkey("ctrl", "f")
    time.sleep(1)
    pag.hotkey("ctrl", "a")
    pag.press("delete")
    pag.typewrite(contact_name)
    time.sleep(1)
    pag.press("tab")
    pag.press("enter")
    time.sleep(1)

    # Message logic
    pag.typewrite("Hola, "+contact_nickname)
    pag.press("enter")
    time.sleep(1)





open_whatsapp()

for i in range(len(contacts)):
    text_contact(contacts[i], contact_nicknames[i])




