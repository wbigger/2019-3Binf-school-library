from Book import Book
from datetime import datetime

class Library:
    def __init__(self, name, sbn_code):
        self.name = name
        self.sbn_code = sbn_code
        self.last_update = datetime.now()
        self.catalogue = []

    def add_to_catalogue(self,book):
        self.catalogue.append(book)
    
    def get_catalogue(self):
        return catalogue