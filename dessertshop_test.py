from dessertshop import *
from freezer import *
from dessert import *
from combine import *

#Test the datatype for DessertItems
def datatype(x):
    myfood = Candy(x, 1.2, 2.5)
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

def checktotalprice(x):
    mycandy = Candy('M&M', 1, x)
    return mycandy.calculate_cost()

def test_checktotalprice():
    assert checktotalprice(100) == 100

def taxes(x):
    mycandy = Candy('M&M', 1, x)
    return mycandy.calculate_tax()

def check_taxes():
    assert taxes(100) == .75
    

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

def checkcookieprice(x):
    mycookie = Cookie('Peanut Butter', 12, x)
    return mycookie.calculate_cost()

def test_checkcookieprice():
    assert checkcookieprice(10) == 10

def checkcookietax(x):
    mycookie = Cookie('Peanut Butter', 12, x)
    return mycookie.calculate_tax()

def test_checkcookietax():
    assert checkcookietax(100) == 7.25
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

def calc_icecream_price(x):
    mycone = IceCream('Vanilla', 10, x)
    return mycone.calculate_cost()

def test_calc_icecream_price():
    assert calc_icecream_price(10) == 100

def icecream_tax_check(x):
    mycone = IceCream('Vanilla', 10, x)
    return mycone.calculate_tax()

def test_icecream_tax_check():
    assert icecream_tax_check(10) == 7.25

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

def calculate_sundae_price(x):
    mysundae = Sundae('Chocolate', 10, 9, 'sprinkles', x)
    return mysundae.calculate_cost()

def test_calculate_sundae_price():
    assert calculate_sundae_price(10) == 100

def calculate_sundae_tax(x):
    mysundae = Sundae('Chocolate', 10, 9, 'sprinkles', x)
    return mysundae.calculate_tax()

def test_calculate_sundae_tax():
    assert calculate_sundae_tax(10) == 7.25

#Test freeze attribute for Cookie, IceCream, and Sundae

def check_chill():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie.chill()
    return mycookie._temperature

def test_check_freeze():
    assert check_chill() == "chilling"

def check_thaw():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie.thaw()
    return mycookie._temperature

def test_check_thaw():
    assert check_thaw() == "thawing"

#check freeze and thaw for icecream

def check_chill():
    myicecream = IceCream('Rocky Road', 3, .5)
    myicecream.chill()
    return myicecream._temperature

def test_check_freeze():
    assert check_chill() == "chilling"

def check_thaw():
    myicecream = IceCream('Rocky Road', 3, .5)
    myicecream.thaw()
    return myicecream._temperature

def test_check_thaw():
    assert check_thaw() == "thawing"

#check freeze and thaw for sundae
def check_chill():
    mysundae = Sundae('3 scoop sundae', 2, 2.24, 'sprinkles', .75)
    mysundae.chill()
    return mysundae._temperature

def test_check_freeze():
    assert check_chill() == "chilling"

def check_thaw():
    mysundae = Sundae('3 scoop sundae', 2, 2.24, 'sprinkles', .75)
    mysundae.thaw()
    return mysundae._temperature

def test_check_thaw():
    assert check_thaw() == "thawing"

#test the __eq__ method for Candy, Cookie, IceCream, and Sundae

def test_candy_eq():
    mycandy = Candy('Butterscotch', 1.2, 2.25)
    mycandy1 = Candy('Butterscotch', 1.2, 2.25)
    assert mycandy == mycandy1

def test_cookie_eq():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 3, 5.5)
    assert mycookie == mycookie1

def test_icecream_eq():
    myicecream = IceCream('Vanchoco', 3, .5)
    myicecream1 = IceCream('Vanchoco', 3, .5)
    assert myicecream == myicecream1

def test_sundae_eq():
    mysundae = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    mysundae1 = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    assert mysundae == mysundae1

#Test __lt__ method for Candy, Cookie, IceCream, and Sundae

def test_candy_lt():
    mycandy = Candy('Butterscotch', 1.1, 2.25)
    mycandy1 = Candy('Butterscotch', 1.2, 2.25)
    assert mycandy < mycandy1

def test_cookie_lt():
    mycookie = Cookie('Chocolate Chip', 2, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 3, 5.5)
    assert mycookie < mycookie1

def test_icecream_lt():
    myicecream = IceCream('Vanchoco', 2, .5)
    myicecream1 = IceCream('Vanchoco', 3, .5)
    assert myicecream < myicecream1

def test_sundae_lt():
    mysundae = Sundae('Hotfudge Sundae', 1, 2.24, 'sprinkles', .74)
    mysundae1 = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    assert mysundae < mysundae1

#Test __gt__ method for Candy, Cookie, IceCream, and Sundae

def test_candy_gt():
    mycandy = Candy('Butterscotch', 1.2, 2.25)
    mycandy1 = Candy('Butterscotch', 1.1, 2.25)
    assert mycandy > mycandy1

def test_cookie_gt():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 2, 5.5)
    assert mycookie > mycookie1

def test_icecream_gt():
    myicecream = IceCream('Vanchoco', 3, .5)
    myicecream1 = IceCream('Vanchoco', 2, .5)
    assert myicecream > myicecream1

def test_sundae_gt():
    mysundae = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    mysundae1 = Sundae('Hotfudge Sundae', 1, 2.24, 'sprinkles', .74)
    assert mysundae > mysundae1

#Test __ge__ method for Candy, Cookie, IceCream, and Sundae

def test_candy_ge():
    mycandy = Candy('Butterscotch', 1.2, 2.25)
    mycandy1 = Candy('Butterscotch', 1.1, 2.25)
    assert mycandy >= mycandy1

def test_cookie_ge():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 2, 5.5)
    assert mycookie >= mycookie1

def test_icecream_ge():
    myicecream = IceCream('Vanchoco', 3, .5)
    myicecream1 = IceCream('Vanchoco', 2, .5)
    assert myicecream >= myicecream1

def test_sundae_ge():
    mysundae = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    mysundae1 = Sundae('Hotfudge Sundae', 1, 2.24, 'sprinkles', .74)
    assert mysundae >= mysundae1

#Test __le__ method for Candy, Cookie, IceCream, and Sundae

def test_candy_le():
    mycandy = Candy('Butterscotch', 1.1, 2.25)
    mycandy1 = Candy('Butterscotch', 1.2, 2.25)
    assert mycandy <= mycandy1

def test_cookie_le():
    mycookie = Cookie('Chocolate Chip', 2, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 3, 5.5)
    assert mycookie <= mycookie1

def test_icecream_le():
    myicecream = IceCream('Vanchoco', 2, .5)
    myicecream1 = IceCream('Vanchoco', 3, .5)
    assert myicecream <= myicecream1

def test_sundae_le():
    mysundae = Sundae('Hotfudge Sundae', 1, 2.24, 'sprinkles', .74)
    mysundae1 = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    assert mysundae <= mysundae1

#Test __ne__ method for Candy, Cookie, IceCream, and Sundae

def test_candy_ne():
    mycandy = Candy('Butterscotch', 1.1, 2.25)
    mycandy1 = Candy('Butterscotch', 1.2, 2.25)
    assert mycandy != mycandy1

def test_cookie_ne():
    mycookie = Cookie('Chocolate Chip', 2, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 3, 5.5)
    assert mycookie != mycookie1

def test_icecream_ne():
    myicecream = IceCream('Vanchoco', 2, .5)
    myicecream1 = IceCream('Vanchoco', 3, .5)
    assert myicecream != myicecream1

def test_sundae_ne():
    mysundae = Sundae('Hotfudge Sundae', 1, 2.24, 'sprinkles', .74)
    mysundae1 = Sundae('Hotfudge Sundae', 2, 2.24, 'sprinkles', .75)
    assert mysundae != mysundae1

#Test can_combine methods for Candy and Cookie

def test_candy_can_combine():
    mycandy = Candy('Butterscotch', 1.1, 2.25)
    mycandy1 = Candy('Butterscotch', 1.2, 2.25)
    assert mycandy.can_combine(mycandy1) == True

def test_cookie_can_combine():
    mycookie = Cookie('Chocolate Chip', 2, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 3, 5.5)
    assert mycookie.can_combine(mycookie1) == True

def test_candy_can_combine_false():
    mycandy = Candy('Butterscotch', 1.1, 2.25)
    mycandy1 = Candy('GummyBears', 1.2, 2.25)
    assert mycandy.can_combine(mycandy1) == False

def test_cookie_can_combine_false():
    mycookie = Cookie('Chocolate Chip', 2, 5.5)
    mycookie1 = Candy('Chocolate Chip', 3, 5.5)
    assert mycookie.can_combine(mycookie1) == False

#Test combine methods for Candy and Cookie

def test_candy_combine():
    mycandy = Candy('Butterscotch', 1.1, 2.25)
    mycandy1 = Candy('Butterscotch', 1.2, 2.25)
    assert mycandy.combine(mycandy1) == Candy('Butterscotch', 2.3, 2.25)

def test_cookie_combine():
    mycookie = Cookie('Chocolate Chip', 2, 5.5)
    mycookie1 = Cookie('Chocolate Chip', 3, 5.5)
    assert mycookie.combine(mycookie1) == Cookie('Chocolate Chip', 5, 5.5)

