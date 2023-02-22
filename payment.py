from enum import Enum

class Payment(Enum):
    #Create payment methods Cash, Card, Phone
    Cash = 1
    Card = 2
    Phone = 3

    def payment_method(self):
        return self.name
