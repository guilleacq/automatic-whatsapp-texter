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

# List of times to send messages (00:02, 00:17, 00:49)
time_to_send = [
    TimeToSend(priority=1, hour=0, minute=2),
    TimeToSend(priority=2, hour=0, minute=12),
    TimeToSend(priority=3, hour=0, minute=41),
]

def open_whatsapp():
    pag.press("winleft")
    time.sleep(1.5)
    pag.typewrite("WhatsApp")
    time.sleep(1)
    pag.press("enter")
    time.sleep(4)
    print("WhatsApp opened")

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
    
    # Get appropriate message (custom or generic)
    message = get_message(contact)
    pag.typewrite(message)
    pag.press("enter")
    time.sleep(1)
    print(f"Message sent to {contact['name']}")

def get_message(contact):
    # Check if there's a custom message
    if contact["customMessage"].strip():
        return contact["customMessage"]
    
    # If no custom message, use generic based on priority
    return get_generic_message(contact["priority"], contact["nickname"])

def get_generic_message(priority, nickname):
    if priority == 1:
        return f"Feliz 2025 {nickname}!!! Sos una persona muy importante para mi, posta espero que arranques este nuevo ciclo con todo. Un abrazo gigantee!"
    elif priority == 2:
        return f"Feliz 2025 {nickname}!! Que empieces muy bien este nuevo ciclo, un fuerte abrazoo"
    elif priority == 3:
        return f"{nickname}, feliz 2025! Un abrazo"

def wait_until(hour, minute):
    target_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    current_time = datetime.datetime.now()
    
    # If target time is in the past for today, set it for tomorrow
    if current_time >= target_time:
        target_time += datetime.timedelta(days=1)
    
    # Wait until the specified time
    wait_seconds = (target_time - datetime.datetime.now()).total_seconds()
    if wait_seconds > 0:
        print(f"Waiting until {hour:02d}:{minute:02d}")
        time.sleep(wait_seconds)

def main():
    # Read contacts from CSV
    reader = CSVReader("contacts.csv")
    contacts = reader.read_contacts()
    
    # Group contacts by priority
    priority_groups = {1: [], 2: [], 3: []}
    for contact in contacts:
        priority_groups[contact["priority"]].append(contact)
    
    # Open WhatsApp once at the start
    open_whatsapp()
    
    # Process each priority group at its specified time
    for time_slot in time_to_send:
        # Wait until the specified time for this priority
        wait_until(time_slot.hour, time_slot.minute)
        
        # Send messages to all contacts in this priority group
        priority_contacts = priority_groups[time_slot.priority]
        print(f"Sending messages to priority {time_slot.priority} contacts")
        for contact in priority_contacts:
            text_contact(contact)

if __name__ == "__main__":
    main()