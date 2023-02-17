from dessert import Cookie, IceCream, Sundae

class Freezer:
    def __init__(self):
        self.myfreezer = []
        self.counter = []

    def freezer(self, item):
        self.freezer.append(item)

    def thaw(self, item):
        self.freezer.remove(item)
        self.counter.append(item)

    #stock freezer with 10 of each cookie, ice cream, and Sundae
    def stock_freezer(self):
        for i in range(10):
            self.myfreezer.append(Cookie('Chocolate Chip Cookie', 12, 3.0))
            self.myfreezer.append(Cookie('Pecan Cookie', 12, 3.25))
            self.myfreezer.append(Cookie('Peanut Butter Cookie', 12, 2.0))
            self.myfreezer.append(IceCream('Vanilla Ice Cream', 1, 2.25))
            self.myfreezer.append(IceCream('Chocolate Ice Cream', 1, 2.25))
            self.myfreezer.append(IceCream('Vanchoco Ice Cream', 1, 4.5))
            self.myfreezer.append(Sundae('Vanilla Ice Cream', 1, 2.25, 'Sprinkles', 1.0))
            self.myfreezer.append(Sundae('Chocolate Ice Cream', 1, 2.25, 'Caramel', 1.0))
            self.myfreezer.append(Sundae('Vanchoco Ice Cream', 1, 4.5, 'Hot Fudge', 1.0))

    def stock_counter(self):
        for i in range(5):
            self.counter.append(Cookie('Chocolate Chip Cookie', 12, 3.0))
            self.counter.append(Cookie('Pecan Cookie', 12, 3.25))
            self.counter.append(Cookie('Peanut Butter Cookie', 12, 2.0))
            self.counter.append(IceCream('Vanilla Ice Cream', 1, 2.25))
            self.counter.append(IceCream('Chocolate Ice Cream', 1, 2.25))
            self.counter.append(IceCream('Vanchoco Ice Cream', 1, 4.5))
            self.counter.append(Sundae('Vanilla Ice Cream', 1, 2.25, 'Sprinkles', 1.0))
            self.counter.append(Sundae('Chocolate Ice Cream', 1, 2.25, 'Caramel', 1.0))
            self.counter.append(Sundae('Vanchoco Ice Cream', 1, 4.5, 'Hot Fudge', 1.0))