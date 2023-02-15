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
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name}           {self.candy_weight}lbs    ${self.price_per_pound}/lbs    ${cost}    ${tax}"


class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity=int, price_per_dozen=float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return self.cookie_quantity / 12 * self.price_per_dozen

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.cookie_quantity}   cookies ${self.price_per_dozen}   ${cost}   ${tax}"

class IceCream(DessertItem):
    def __init__(self, name, scoop_count=int, price_per_scoop=float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.scoop_count} scoops   {self.price_per_scoop}/scoop    ${cost}   ${tax}"
    

class Sundae(IceCream):
    def __init__(self,name, scoop_count=int, price_per_scoop=float, topping_name=str, topping_price=float):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.scoop_count} scoops ${self.price_per_scoop}/scoop {self.topping_name} ${self.topping_price} ${cost} ${tax}"
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

    def print_order(self):
        print("_____________________________________________________")
        print("Name        Quantity    Unit    Price    Cost    Tax")
        print("_____________________________________________________")    

        for item in self.order:
            print(item)
            print('')

def main_menu(my_order: Order) -> None:
    continue_order = True
    while continue_order == True:
        print('Type the number of the option you would like to choose: ')
        print('1: Candy')
        print('2: Cookies')
        print('3: IceCream')
        print('4: Sundae')
        print('5: Total Order So Far')
        print('Hit enter with no input to print your receipt')
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
        elif choice == '5':
            print(my_order)
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
        candy = "m&m's"
        price = 4.0
    elif candy == "":
        print('Returning to main menu')
        main_menu()
    else:
        print('Invalid Input: please use the prompts provided')
        user_prompt_candy(my_order)

    weight = input('How many lbs of candy would you like? ')
    weight = float(weight)
    print(f'Adding {weight} lbs of {candy} to your order.'.format(weight, candy))

    candy_item = Candy(candy,weight, price )
    my_order.add_item(candy_item)



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
        user_prompt_cookie(my_order)
    else:
        print("Invalid syntax:  Please use the options provided")
        user_prompt_cookie(my_order)

    amount = input('How many cookies would you like? ')
    amount = int(amount)

    cookie_item = Cookie(cookie, amount, price)
    my_order.add_item(cookie_item)

def user_prompt_icecream(my_order):
    print('1. Vanilla ($2.25 per scoop) 2. Chocolate ($2.25 per scoop) 3. Vanchoco ($4.50 per scoop)')
    icecream = input('Which flavor would you like to try? ')
    if icecream == '1':
        icecream = 'Vanilla Ice Cream'
        price = 2.25
    elif icecream == '2':
        icecream = 'Chocolate Ice Cream'
        price = 2.25
    elif icecream == '3':
        icecream = 'Vanchoco Ice Cream'
        price = 4.5
    elif icecream == '':
        main_menu(my_order)
    else:
        print('Improper syntax: please use the provided menu')
        print(type(icecream))
        user_prompt_icecream(my_order)

    scoops = input('How many scoops would you like? ')
    scoops = int(scoops)

    icecream_item = IceCream(icecream, scoops, price)
    my_order.add_item(icecream_item)
    print(f'Adding a {icecream} flavored Ice Cream with {scoops} scoops'.format(icecream, scoops))
    
def user_prompt_sundae(my_order):
    print('1. Vanilla ($2.25 per scoop) 2. Chocolate ($2.25 per scoop) 3. Vanchoco ($4.50 per scoop)')
    icecream = input('Which flavor would you like to try? ')
    if icecream == '1':
        icecream = 'Vanilla Ice Cream'
        price = 2.25
    elif icecream == '2':
        icecream = 'Chocolate Ice Cream'
        price = 2.25
    elif icecream == '3':
        icecream = 'Vanchoco Ice Cream'
        price = 4.5
    elif icecream == '':
        main_menu(my_order)
    else:
        print('Improper syntax: please use the provided menu')
        user_prompt_sundae(my_order)

    scoops = input('How many scoops would you like? ')
    scoops = int(scoops)

    
    print('1. Sprinkles (.25 cents) 2. Caramel (.50 cents) 3. Gummy Bears (.30 cents)')
    topping = input('What topping would you like?')
    
    if topping == '1':
        topping = 'Sprinkles'
        topprice = .25
    elif topping == '2':
        topping == "Caramel"
        topprice = .50
    elif topping == '3':
        topping = 'Gummy Bears'
        topprice = .30
    elif topping == '':
        main_menu()
    else:
        print('Invalid input: Please use the menu options')

    print(f'Adding a {icecream} flavored sundae with {topping} on top'.format(icecream, topping))

    sundae_item = Sundae(icecream, scoops, price, topping, topprice)
    my_order.add_item(sundae_item)
    
    


def main():
   
    my_order = Order()

    try:
        main_menu(my_order)
    except:
        main_menu(my_order)
        
    my_order.print_order()

    cost = round(my_order.order_cost(), 2)
    tax = round(my_order.order_tax(), 2)
    total_cost = cost + tax
    make_receipt(my_order.order, "receipt.pdf", cost, total_cost)



if __name__ == "__main__":
    main()
