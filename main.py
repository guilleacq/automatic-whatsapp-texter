# Author: guilleacq
# WARNING: This code may work differently in different systems and responses may vary based on PC performance / operating system. 
# I am not responsible for any damage you may cause to your reputation/pc if this works in an unexpected way
# Also, by using this YOU ARE LETTING A PROGRAM MANAGE YOUR COMPUTER and it CANNOT be stopped UNLESS you force stop the process (Ctrl + C). 
# --------------------------------------------------- USE AT YOUR OWN RISK ----------------------------------------------

import pyautogui as pag 
import time
import datetime
from csv_reader import CSVReader
from time_to_send import TimeToSend

# List of times to send messages
time_to_send = [
    TimeToSend(priority=1, hour=0, minute=8),
    TimeToSend(priority=2, hour=0, minute=12),
    TimeToSend(priority=3, hour=0, minute=26),
]

contacts = []

def open_whatsapp():
    pag.press("winleft")
    time.sleep(1.5)
    pag.typewrite("WhatsApp")
    time.sleep(1)
    pag.press("enter")
    time.sleep(4)
    print("WhatsApp opened")

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
    message = get_generic_message(contact["priority"], contact["nickname"])
    pag.typewrite(message)
    pag.press("enter")
    time.sleep(1)

# TODO: Fix this (can't type letter ñ)
def get_generic_message(priority, nickname):
    if priority == 1:
        return f"Feliz año nuevoo {nickname}!! Sos una persona muy importante para mi, espero que este año sea increible para vos. Un abrazo gigante!"
    elif priority == 2:
        return f"Feliz añoo {nickname}!! Que empieces muy bien este 2025"
    elif priority == 3:
        return f"{nickname}, feliz 2025! Un abrazo"


def main(): 
    reader = CSVReader("contacts.csv")
    contacts = reader.read_contacts()

    open_whatsapp()

    for contact in contacts:
        text_contact(contact)

    # current_time = datetime.datetime.now()


if __name__ == "__main__":
    main()