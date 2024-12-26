import csv

class CSVReader:

    def __init__ (self, file_path):
        self.file_path = file_path

    def read_contacts(self):
        contacts = []

        with open(self.file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                contact = {
                    "name": row["name"],
                    "nickname": row["nickname"],
                    "priority": int(row["priority"]),
                    "customMessage": row["customMessage"]
                }

                contacts.append(contact)
        return contacts
    

    
