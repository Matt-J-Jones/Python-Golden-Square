class Contact:
    def __init__(self, contact):
        self.contact = {"Name": contact[0], "Number": contact[1]}
    
    def return_contact(self):
        return self.contact["Name"] + ": " + str(self.contact["Number"])
