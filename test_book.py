from Book import Book
from datetime import datetime

def create_book(year):
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

def test_title():
    harry_potter = create_book(1)
    assert harry_potter.title == "Harry Potter e la pietra filosofale"

def test_author():
    harry_potter = create_book(1)
    assert harry_potter.author == "J. K. Rowling"    

def test_publisher():
    harry_potter = create_book(1)
    assert harry_potter.publisher == "Salani Editore"

def test_year():
    harry_potter = create_book(1)
    assert harry_potter.year == 1997    

def test_pages():
    harry_potter = create_book(5)
    assert harry_potter.pages == 738  

def test_isbn():
    harry_potter = create_book(1)
    assert harry_potter.isbn == 8877827025

def test_bulky_1():
    # se il libro ha più di 500 pagine, è ingombrante (bulky)
    harry_potter = create_book(1)
    assert harry_potter.is_bulky == False

def test_bulky_2():
    harry_potter = create_book(5)
    assert harry_potter.is_bulky == True

def test_bulky_3():
    harry_potter = create_book(6)
    assert harry_potter.is_bulky == False


def test_valuable_1():
    # Un libro è pregiato (valuable) se ha più di 20 anni o meno di un anno
    harry_potter = create_book(1)
    # is valuable prende in input l'anno presente
    # in python per prendere l'anno corrente, si può usare
    # la libreria datetime come segue
    assert harry_potter.is_valuable(datetime.now().year) == True

def test_valuable_2():
    harry_potter = create_book(7)
    assert harry_potter.is_valuable(datetime.now().year) == False

def test_valuable_3():
    harry_potter = create_book(6)
    assert harry_potter.is_valuable(2005) == True

def test_valuable_4():
    harry_potter = create_book(7)
    assert harry_potter.is_valuable(2030) == True    

def test_isbn_1():
    # Assuming the digits are "abcdefghi-j" where j is the check digit. Then the check digit is computed by the following formula:
    # j = ( [a b c d e f g h i] * [1 2 3 4 5 6 7 8 9] ) mod 11 
    harry_potter = create_book(1)
    assert harry_potter.is_isbn_valid() == True

def test_isbn_2():
    # Assuming the digits are "abcdefghi-j" where j is the check digit. Then the check digit is computed by the following formula:
    # j = ( [a b c d e f g h i] * [1 2 3 4 5 6 7 8 9] ) mod 11 
    harry_potter = create_book(4)
    assert harry_potter.is_isbn_valid() == False