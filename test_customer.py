from dessertshop import Customer
import random
import string

#Tests for Customer class

def test_customer_name():
    newcustomer = Customer('John')
    assert newcustomer.name == 'John'

def test_customer_class():
    newcustomer = Customer('John')
    assert isinstance(newcustomer, Customer)

#Test that customerid is always unique
def test_customer_id():
    #list to store random strings which will be used to generate unique customers
    listostrings = []
    #generate random string
    N = 10
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    if res in listostrings:
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    else:
        listostrings.append(res)
    #list to store customer ids
    customerlist = []
    #generate 10000 customers
    for i in range(10000):
        newcustomer = Customer(res)
        newcustomer.figure_customerid(customerlist)
        customerlist.append(newcustomer.customerid)
    #check that all customer ids are unique by taking advantage of the fact that sets cannot contain duplicates
    #if there are duplicates in the list it will fail to assert because it cannot create the customer list set
    assert len(customerlist) == len(set(customerlist))
