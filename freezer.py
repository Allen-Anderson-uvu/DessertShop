from dessert import DessertItem, Cookie, IceCream, Sundae
from typing import Protocol

class Freeze(Protocol):
    _temperature = "thawing"

    def chill(self) -> None:
        self._temperature = "chilling"

    def thaw(self) -> None:
        self._temperature = "thawing"

    def get_temperature(self) -> str:
        return getattr(self, '_temperature', 'thawing')

    
class Freezer:
    def __init__(self):
        self.freezer = []
        self.counter = []

    def freeze(self, item):
        self.freezer.append(item)

    def thaw(self, item):
        self.freezer.remove(item)
        self.counter.append(item)

    #stock freezer with 10 of each cookie, ice cream, and Sundae
    def stock_freezer(self):
        for i in range(10):
            self.freezer.append(Cookie('Chocolate Chip Cookie', 12, 3.0))
            self.freezer.append(Cookie('Pecan Cookie', 12, 3.25))
            self.freezer.append(Cookie('Peanut Butter Cookie', 12, 2.0))
            self.freezer.append(IceCream('Vanilla Ice Cream', 1, 2.25))
            self.freezer.append(IceCream('Chocolate Ice Cream', 1, 2.25))
            self.freezer.append(IceCream('Vanchoco Ice Cream', 1, 4.5))
            self.freezer.append(Sundae('Vanilla Ice Cream', 1, 2.25, 'Sprinkles', 1.0))
            self.freezer.append(Sundae('Chocolate Ice Cream', 1, 2.25, 'Caramel', 1.0))
            self.freezer.append(Sundae('Vanchoco Ice Cream', 1, 4.5, 'Hot Fudge', 1.0))

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