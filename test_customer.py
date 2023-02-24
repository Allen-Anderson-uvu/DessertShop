from dessertshop import Customer

#Tests for Customer class

def test_customer_name():
    newcustomer = Customer('John')
    assert newcustomer.name == 'John'

def test_customer_class():
    newcustomer = Customer('John')
    assert isinstance(newcustomer, Customer)