#I want to create a code that can easily be adjusted if offers change, new items are added or prices change.
#Therefore, I thought a class was best to clearly lay out the items and offers.
#TO get cost, call Checkout(string).totalCost()

import math

class Checkout:

    def __init__(self, cart):

        #Initialize the cart and total value of cart
        self.cart = cart
        self.total = 0

        #Mapping of items to their values
        self.itemValue = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 10,
        }

        #Mapping of item to its offer in a tuple. Tuple[0] is the num for discount and tuple[1] is the discount
        self.offers = {
            'A' : (3, 130),
            'B' : (2, 37)
        }

    
    #A function that takes in the current total of cart and applys the discount for the item
    def offer(self, discountItem, num, value):
        #Number of items in cart
        cnt = 0
        for item in self.cart:
            if item == discountItem:
                cnt+=1

        #Find the amount of discounts applied and the discount
        numOfDiscounts = math.floor(cnt/num) 
        discount = numOfDiscounts * (num * self.itemValue[discountItem]- value)
        
        self.total -= discount

    def totalCost(self):

        #Iterate through each item and add its value to total
        #If item does not exist in the items listed for sale, return invalid message
        for item in self.cart:
            if item in self.itemValue:
                self.total += self.itemValue[item]
            else:
                return 'Sorry, item '+str(item)+' not currently available for purchase.'

        #Apply offers    
        for itemOffer in self.offers:
            numForDiscount = self.offers[itemOffer][0]
            discount = self.offers[itemOffer][1]
            self.offer(itemOffer, numForDiscount, discount)

    
        return self.total

