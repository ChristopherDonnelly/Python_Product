'''
The owner of a store wants a program to track products. Create a product class to fill the following requirements.

Product Class:
Attributes:

• Price
• Item Name
• Weight
• Brand
• Status: default "for sale"

Methods:

• Sell: changes status to "sold"
• Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
• Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
• Display Info: show all product details.

Every method that doesn't have to return something should return self so methods can be chained.
'''

class Product(object):
    def __init__(self, price, name, weight, brand, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

        self.display_info()
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax_amount):
        taxed = ((tax_amount / 100) * self.price) + self.price
        returnAmount = ''
        if self.status != 'defective':
            returnAmount = self.name+' - Price with Sales Tax: $' + str(round(taxed, 2)) + '\n'
        else:
            returnAmount = self.name+' - This product is defective and cannot be sold\n'

        return returnAmount
    def add_discount(self, discount_amount):
        self.price -= ((discount_amount / 100) * self.price)

        return self
    def return_item(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in box' or reason == 'like new':
            self.status = 'for sale'
        elif reason == 'used' or reason == 'opened':
            self.status = 'used'
            self.add_discount(20.0)

        print 'Returned', self.name, 'as', reason

        self.display_info()
        return self
    def display_info(self):
        print 'Name:', self.name, '\nBrand:', self.brand, '\nPrice: ${0:.2f}'.format(self.price, 2), '\nStatus:', self.status, '\nWeight:', self.weight, '\n'
        return self

gobstopper = Product(1000000.00, 'Everlasting Gobstopper', 0.5, 'Willy Wonka', 'not for sale')
triple_cream = Product(1.00, 'Triple Cream Cup', 0.75, 'Willy Wonka')
squanch = Product(2.00, 'Squelchy Snorter', 1.0, 'Willy Wonka')
sizzler = Product(2.50, "Slugworth’s Sizzler", 0.25, 'Willy Wonka')

print squanch.add_tax(8.25)
squanch.return_item('used')
print squanch.add_tax(8.25)
squanch.return_item('defective')
print squanch.add_tax(8.25)
