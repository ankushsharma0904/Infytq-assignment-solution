'''
A vendor at a food court is in the process of automating his order management system.
The vendor serves the following menu – Veg Roll, Noodles, Fried Rice and Soup and also
maintains the quantity available for each item. The customer can order any combination of items.
The customer is provided the item if the requested quantity of item is available with the vendor.


Write a python program which implements the following functions.
place_order(*item_tuple): This function accepts the order placed by the customer.
Consider it to be a variable length argument as each customer may have a different order.
The function should check whether the items requested are present in the vendor’s menu and if so,
it should check whether the requested quantity is available for each by invoking the
check_quantity_available() method.


The function should display appropriate messages for each item in the order for the below scenarios:

When the requested item is not available in vendor’s menu, display <Item Name> is not available
When the quantity requested by the customer is not available, display <Item Name> stock is over
When the requested quantity of the item is available with the vendor, display <Item Name> is available

check_quantity_available(index,quantity_requested): This function should check whether the requested
quantity of the specified item is available. If so, it should reduce the quantity requested from the
quantity available for that item and return True. Otherwise, it should return False.
'''
#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    #Remove pass and write your logic here
    for item in range(0, len(item_tuple), 2):
        if item_tuple[item] not in menu:
            print(item_tuple[item], "is not available")
            continue
        
        index = menu.index(item_tuple[item])
        
        if not(check_quantity_available(index, item_tuple[item+1])):
            print(item_tuple[item], "stock is over")
            continue
        
        else:
            quantity_available[index] -= item_tuple[item+1]
            print (item_tuple[item], "is available")

    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    #Remove pass and write your logic here to return an appropriate boolean value
    if quantity_available[index] >= quantity_requested: return True
    return False


#Provide different values for items ordered and test your program
place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)
