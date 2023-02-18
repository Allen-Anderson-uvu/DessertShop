from receipt import *
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
from freezer import Freezer, Freeze


class Order:
    # Class that represents an order of items from the dessert shop
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
        print("-----------------------RECEIPT-----------------------")
        print("_____________________________________________________")
        print("Name        Quantity      Price         Cost     Tax")
        print("_____________________________________________________")    

        for item in self.order:
            print(item)
            print('')
        print("_____________________________________________________")
        print(f"Total Cost: ${self.order_cost():.2f}   Total Tax: ${self.order_tax():.2f}")

# Stock the freezer with ten of each icecream, cookie, and sundae, call freeze on each item, and return the freezer
def stock_freezer():
    freezer = Freezer()
    for i in range(10):
        freezer.add_2_freezer(IceCream('Vanilla', 3, .5))
        freezer.add_2_freezer(IceCream('Chocolate', 3, .5))
        freezer.add_2_freezer(IceCream('Vanchoco', 3, .5))
        freezer.add_2_freezer(Cookie('Chocolate Chip', 3, 5.5))
        freezer.add_2_freezer(Cookie('Peanut Butter', 3, 5.5))
        freezer.add_2_freezer(Cookie('Pecan', 3, 5.5))
        freezer.add_2_freezer(Sundae('Vanilla', 3, .5, 'Sprinkles'))
        freezer.add_2_freezer(Sundae('Chocolate', 3, .5, 'Caramel'))
        freezer.add_2_freezer(Sundae('Vanchoco', 3, .5, 'Gummy Bears'))
    #Chill items in the freezer
    for i in freezer.my_freezer:
        i.chill()
    return freezer


def main_menu(my_order: Order, freezer) -> None:
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
            user_prompt_cookie(my_order, freezer)
        elif choice == '3':
            user_prompt_icecream(my_order, freezer)
        elif choice == '4':
            user_prompt_sundae(my_order, freezer)
        elif choice == '':
            continue_order = False
        elif choice == '5':
            print(my_order)
        else:
            print("Invalid input, please use the provided interface.")


def user_prompt_candy(my_order):
    #Prompts user for candy type and amount
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



def user_prompt_cookie(my_order, freezer):
    #Prompts user for cookie type and amount
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
    #Takes item out of the freezer or makes it from scratch if it is not in the freezer
    cookie_found = False
    for item in freezer.my_freezer:
        if item.name == cookie_item.name:
            item.thaw()
            freezer.my_freezer.remove(item)
            my_order.add_item(item)
            cookie_found = True
            break

    if not cookie_found:
        my_order.add_item(cookie_item)



def user_prompt_icecream(my_order, freezer):
    #Prompts user for icecream flavor and amount
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
    #Take item out of the freezer or makes it from scratch if it is not in the freezer
    icecream_found = False
    for item in freezer.my_freezer:
        if item.name == icecream_item.name:
            item.thaw()
            freezer.my_freezer.remove(item)
            my_order.add_item(item)
            icecream_found = True
            break
    
    if not icecream_found:
        my_order.add_item(icecream_item)

    print(f'Adding a {icecream} flavored Ice Cream with {scoops} scoops'.format(icecream, scoops))
    
def user_prompt_sundae(my_order, freezer):
    #This function is a little different than the others because it is a combination of two other items, ice cream and toppings
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
    #Take item out of the freezer or makes it from scratch if it is not in the freezer, match topping to ice cream
    sundae_found = False
    for item in freezer.my_freezer:
        if item.name == sundae_item.name and item.topping == sundae_item.topping:
            item.thaw()
            freezer.my_freezer.remove(item)
            my_order.add_item(item)
            sundae_found = True
            break
    
    if not sundae_found:
        my_order.add_item(sundae_item)

def main():

    freezer = stock_freezer()
   
    my_order = Order()

    try:
        main_menu(my_order, freezer)
    except:
        main_menu(my_order, freezer)
        
    my_order.print_order()

    cost = round(my_order.order_cost(), 2)
    tax = round(my_order.order_tax(), 2)
    total_cost = cost + tax
    make_receipt(my_order.order, "receipt.pdf", cost, total_cost)



if __name__ == "__main__":
    main()
