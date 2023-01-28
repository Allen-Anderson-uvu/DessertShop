from dessertshop import *

#Test the datatype for DessertItems
def datatype(x):
    myfood = DessertItem(x)
    return myfood.name

def test_datatype():
    assert datatype('cake') == 'cake'

#Test Candy constructors

def checkweight(x):
    mycandy = Candy('Butterscotch', 1.2, 2.25)
    mycandy.candy_weight += x
    return mycandy.candy_weight

def test_checkweight():
    assert checkweight(1.2) == 2.4

def checkprice(x):
    mycandy = Candy('Butterscotch', 1.2, 2.25)
    mycandy.price_per_pound += x
    return mycandy.price_per_pound

def test_checkprice():
    assert checkprice(1.2) == 3.45 
    

#test the cookie constructors

def number_of_cookies(x):
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie.cookie_quantity = mycookie.cookie_quantity + x
    return mycookie.cookie_quantity

def test_number_of_cookies():
    assert number_of_cookies(3) == 6

def cookieprice(x):
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie.price_per_dozen += x
    return mycookie.price_per_dozen

def test_cookieprice():
    assert cookieprice(5.5) == 11.0

#Test IceCream constructors

def countscoops(x):
    mycone = IceCream('Rocky Road', 3, .5)
    mycone.scoop_count += x
    return mycone.scoop_count

def test_scoops():
    assert countscoops(1) == 4

def checkprice(x):
    mycone1 = IceCream('Rocky Road', 3, 1.5)
    mycone1.price_per_scoop += x
    return mycone1.price_per_scoop

def test_checkprice():
    assert checkprice(2.5) == 4.0

#Test Sundae constructors
def sundaetopping(x):
    mysundae = Sundae('3 scoop sundae', 2, 2.24, x, .75)
    return mysundae.topping_name

def test_sundaetopping():
    sundaetopping('sprinkles') == 'sprinkles'

def pricecheck(x):
    mysundae = Sundae('3 scoop sundae', 2, 2.24, x, .75)
    mysundae.topping_price += x
    return mysundae.topping_price

def test_pricecheck():
    assert pricecheck(1) == 1.75