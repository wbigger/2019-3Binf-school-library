from Book import Book

class BookFactory:

    @staticmethod
    def create(year):
        if year == 1:
            return Book("Harry Potter e la pietra filosofale","J. K. Rowling","Salani Editore",1997, 294, 8877827025)
        elif year == 2:
            return Book("Harry Potter e la camera dei segreti","J. K. Rowling","Salani Editore",1998, 289, 8877827033)
        elif year == 3:
            return Book("Harry Potter e il prigioniero di Azkaban","J. K. Rowling","Salani Editore",1999, 341, 8877828528)
        elif year == 4:
            return Book("Harry Potter e il calice di fuoco","J. K. Rowling","Salani Editore",2000, 571, 8884510490)
        elif year == 5:
            return Book("Harry Potter e l'ordine della fenice","J. K. Rowling","Salani Editore",2003, 738, 8884513448)
        elif year == 6:
            return Book("Harry Potter e il principe mezzosangue","J. K. Rowling","Salani Editore",2005, 486, 8884516374)
        elif year == 7:
            return Book("Harry Potter e i doni della morte","J. K. Rowling","Salani Editore",2007, 557, 9788884518781)
