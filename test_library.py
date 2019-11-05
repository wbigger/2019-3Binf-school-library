from BookFactory import BookFactory
from Library import Library

def create_library():
    return Library("IIS Marconi","CIVMA")

def test_init_name():
    library = create_library()
    assert library.name == "IIS Marconi"
    
    #book = BookFactory.create(1)
    #print(book.title)


