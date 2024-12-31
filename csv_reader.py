import csv

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_contacts(self):
        contacts = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    try:
                        contact = {
                            "name": row["name"].strip(),
                            "nickname": row["nickname"].strip(),
                            "priority": int(row["priority"]),
                            "customMessage": row["customMessage"].strip() if row["customMessage"] else ""
                        }
                        contacts.append(contact)
                    except KeyError as e:
                        print(f"Error: '{e}' row missing in CSV.")
                    except ValueError:
                        print(f"Error: The priority must be an integer in row: {row}")
        except FileNotFoundError:
            print(f"Error: File was not found at '{self.file_path}'.")
        return contacts