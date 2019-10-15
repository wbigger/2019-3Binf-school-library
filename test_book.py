from main import Book 

def test_book_title():
    harry_potter = Book("Harry Potter e il calice di fuoco", "J.K.Rowling",1)
    assert harry_potter.title == "Harry Potter e il calice di fuoco"