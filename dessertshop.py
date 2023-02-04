from abc import ABC, abstractmethod
from receipt import *

class DessertItem(ABC):
    def __init__(self, name=str):
        self.name = name
        self.tax_percent = 7.25

    def __str__(self):
        return self.name

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)

class Candy(DessertItem):
    def __init__(self, name, candy_weight= float, price_per_pound=float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound


class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity=int, price_per_dozen=float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return self.cookie_quantity / 12 * self.price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name, scoop_count=int, price_per_scoop=float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop
    

class Sundae(IceCream):
    def __init__(self,name, scoop_count=int, price_per_scoop=float, topping_name=str, topping_price=float):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

class Order:
    def __init__(self):
        self.order = []

    def add_item(self, item):
        self.order.append(item)
 
    def __len__(self):
        return len(self.order)

    def order_cost(self):
        total_cost = 0
        for items in self.order:
            total_cost += items.calculate_cost()
        return round(total_cost, 2)

    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()

        return round(total_tax, 2)

def main_menu(my_order):
    continue_order = True
    while continue_order == True:
        print('Type the number of the option you would like to choose: ')
        print('1: Candy')
        print('2: Cookies')
        print('3: IceCream')
        print('4: Sundae')
        print('5: Total Order So Far')
        choice = input('Choose an option: ')

        if choice == '1':
            user_prompt_candy(my_order)
        elif choice == '2':
            user_prompt_cookie(my_order)
        elif choice == '3':
            user_prompt_icecream(my_order)
        elif choice == '4':
            user_prompt_sundae(my_order)
        elif choice == '':
            continue_order = False
        else:
            print("Invalid input, please use the provided interface.")

def user_prompt_candy(my_order):
    print('1: Butterscotch ($2.25 per lbs) 2: Caramel (.50 per lbs) 3: m&m ($4.00 per lbs)')
    candy = input("What kind of candy would you like? :")
    if candy == '1':
        candy = 'Butterscotch'
        price = 2.25
    elif candy == '2':
        candy = 'Caramel'
        price = .5
    elif candy == '3':
        candy == "m&m's"
        price = 4.0
    elif candy == "":
        print('Returning to main menu')
        main_menu()
    else:
        print('Invalid Input: please use the prompts provided')
        user_prompt_candy(my_order)

    weight = input('How many lbs of candy would you like? ')
    weight = float(weight)
    print('Adding', weight, 'lbs of', candy, 'to your order.')

    my_order.append(('Candy', candy, price, weight))



def user_prompt_cookie(my_order):
    print('1. Chocolate Chip ($3.00 per dozen) 2. Pecan ($3.25 per dozen) 3. Peanut Butter ($2.00 per dozen)')
    cookie = input('Which cookie would you like to order? ')

    if cookie == '1':
        cookie = "Chocolate Chip Cookie"
        price = 3.0
    elif cookie == '2':
        cookie = "Pecan Cookie"
        price = 3.25
    elif cookie == '3':
        cookie = "Peanut Butter Cookie"
        price = 2.0
    elif cookie == "":
        main_menu()
    else:
        print("Invalid syntax:  Please use the options provided")
        user_prompt_cookie(my_order)

    amount = input('How many cookies would you like? ')
    amount = int(amount)

    my_order.append(('Cookie', cookie, price, amount))

def user_prompt_icecream(my_order):
    print('1. Vanilla ($2.25 per scoop) 2. Chocolate ($2.25 per scoop) 3. Vanchoco ($4.50 per scoop)')
    icecream = input('Which flavor would you like to try? ')
    if input == '1':
        icecream = 'Vanilla Ice Cream'
        price = 2.25
    elif input == '2':
        icecream = 'Chocolate Ice Cream'
        price = 2.25
    elif input == '3':
        icecream = 'Vanchoco Ice Cream'
        price = 4.5
    elif icecream == '':
        main_menu(my_order)
    
def user_prompt_sundae():
    pass


def main():
    my_order = []

    main_menu(my_order)
    print(my_order)

     # Create an instance of the Order class
    # my_order = Order()

    # Add items to the order
    # Add items to the order
    # my_order.add_item(Candy("Candy Corn", 1, 3.0))
    # my_order.add_item(Candy("Gummy Bears", 2, 4.0))
    # my_order.add_item(Cookie("Chocolate Chip", 2, 2.0))
    # my_order.add_item(Cookie("Pistachio Cookie", 1, 3.0))
    # my_order.add_item(IceCream("Vanilla", 3, 2.0))
    # my_order.add_item(Cookie("Oatmeal Raisin", 2, 5.0))




    # # Calculate the cost and tax of the order
    # cost = round(my_order.order_cost(), 2)
    # tax = round(my_order.order_tax(), 2)
    # total_cost = cost + tax

    # make_receipt(my_order.order, "receipt.pdf", cost, total_cost)



if __name__ == "__main__":
    main()
