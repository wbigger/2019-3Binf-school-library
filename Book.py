class Book:
    def __init__(self,title,author,publisher,year, pages, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn
        self.is_bulky = self.pages > 500
        
    def is_valuable(self,current_year):
        return current_year - self.year > 20 or current_year - self.year < 1
    
    def is_isbn_valid(self):
        idx = 1
        accumulator = 0
        for i in str(self.isbn)[:-1]:
            accumulator += int(i) * idx
            idx +=1
        accumulator = accumulator % 11
        return accumulator == int(str(self.isbn)[-1:])
