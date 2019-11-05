from Locker import Locker
from datetime import datetime

def create_locker(number):
    if number == 1:
        return Locker("Corridorio piano terra",180,200,60, "legno massello",6)
    elif number == 2:
        return Locker("Sala professori",160,180,50, "metallo leggero",9)
    elif number == 3:
        return Locker("Primo piano",160,180,50, "metallo blindato",5)
    elif number == 4:
        return Locker("Secondo piano",160,180,50, "legno e vetro",8)
    elif number == 5:
        return Locker("Palazzina 1",180,200,60, "truciolato",2)
    elif number == 6:
        return Locker("Palazzina 2",180,200,60, "legno massello",9)
    elif number == 7:
        return Locker("Atrio piano terra",160,180,50,"metallo blindato",7)

def test_name():
    locker = create_locker(1)
    assert locker.position == "Corridorio piano terra"

def test_width():
    locker = create_locker(1)
    assert locker.width == 180

def test_height():
    locker = create_locker(1)
    assert locker.height == 200

def test_depth():
    locker = create_locker(1)
    assert locker.depth == 60    

def test_material():
    locker = create_locker(1)
    assert locker.material == "legno massello"

def test_private_key():
    locker = create_locker(1)
    assert locker.private_key == 6

def test_bulky_1():
    # se il volume del locker è maggiore di 2 metri cubi
    # allora il locker è ingombrante
    locker = create_locker(1)
    assert locker.is_bulky == True

def test_bulky_2():
    locker = create_locker(2)
    assert locker.is_bulky == False

def test_bulky_3():
    locker = create_locker(6)
    assert locker.is_bulky == True


def test_is_valid_1():
    # Un codice inserito è valido se è compreso fra i 4 e gli 8 caratteri
    locker = create_locker(1)
    # per sapere la lunghezza di una stringa potete usare la funzione len()
    assert locker.is_code_valid("ABA") == False

def test_is_valid_2():
    locker = create_locker(7)
    assert locker.is_code_valid("ABAB") == True

def test_is_valid_3():
    locker = create_locker(6)
    assert locker.is_code_valid("ABABBAAAA") == False

def test_is_valid_4():
    locker = create_locker(7)
    assert locker.is_code_valid("ABABBA") == True    

def test_secret_1():
    # Assuming that, in code, the value of "A" is 1 and "B" is 2,
    # and the code is "abcdef", then the secret is true by the following formula:
    # (a+b+c+d+e+f) mod (private_key) == 0
    locker = create_locker(1)
    assert locker.is_secret_passed("ABAB") == True

def test_secret_2():
    locker = create_locker(2)
    assert locker.is_secret_passed("ABAB") == False