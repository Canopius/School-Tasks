import pyinputplus as pyip
from datetime import *

ShopInventory = {"Red Sweet": 0.5, "Green Sweet" : 0.5, "Blue Sweet" : 0.5}
ShoppingBasket = {}
Item, Qty= False, False


def ChooseProduct():
    Item = pyip.inputMenu(["Red Sweet", "Green Sweet", "Blue Sweet"], prompt = "\nPlease select one of the following:\n", numbered = True)
    Qty = pyip.inputInt(prompt = "\nQty: ", min=1)

    if Item in ShoppingBasket:
        ShoppingBasket[Item] += Qty
    else:
        ShoppingBasket[Item] = Qty
    

def CalculateTotal():
    Total = 0
    for x, y in ShoppingBasket.items():
        Total += ShopInventory[x] * y

    Discount = 1

    if Total > 25:
        Discount -= 0.1
    elif Total > 10:
        Discount -= 0.25

    return Total * Discount

def ContinueShopping():
    if pyip.inputYesNo(prompt = "\nWould you like more items? ") == "no":
        return False
    else:
        return True

def DeliveryDate():
    Today = date.today()
    Delivery = pyip.inputDate(prompt= "\nWhen would you like your order delivered? (YYYY/MM/DD) ")
    x = (Delivery - Today).total_seconds()
    
    if x > 86400:
        return Delivery
    else:
        return False


def Main():
    
    MoreItems = True
    while MoreItems:
        ChooseProduct()
        print("\nSub-total: £{}".format(CalculateTotal()))
        MoreItems = ContinueShopping()

    print("\nGrand Total: £{}".format(CalculateTotal()))

    NoDate = True
    while NoDate:
        Date = DeliveryDate()
        if Date:
            print("\nYour delivery will arrive on {}".format(Date))
            NoDate = False
        else:
            print("\nIt takes at least 1 day to deliver your order, please select a different date.")

Main()
"""
try:
    Main()
except:
    print("\nAn error has occured\n")
"""