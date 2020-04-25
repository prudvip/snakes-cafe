from textwrap import dedent

welcome_text ="""**************************************
    **    Snakes Cafe   **
*
*
        **    MENU   **

** To quit at any time, type "quit" **
**************************************"""

order_text ="""***********************************
** Please place your order **
***********************************
"""

menu_item = {
    "Appetizers":{
        "fries": 0,
        "cutlet": 0,
        "veg rolls": 0
    },
    "Entrees":{
        "meat burger": 0,
        "chicken burger": 0,
        "fish cookies": 0,
        "veg salad": 0
    },
    "Desserts":{
        "apple pie": 0,
        "cake pudding": 0,
        "caramel custard": 0
    },
    "Drinks":{
        "black coffee": 0,
        "irish coffee": 0,
        "ice tea": 0
    }
}

def print_menuitems():
    for itemType in menu_item:        
        print(dedent(f"""
        {itemType}
        ----------"""))        
        for item in menu_item[itemType]:            
            print(item.title())
        print("\n")


def take_order_details(order_input):
    for itemType in menu_item:
        current_Item_Type = menu_item[itemType]
        for item in current_Item_Type:
            if order_input == item:
                quantity = current_Item_Type[order_input]
                quantity += 1
                current_Item_Type[order_input] = quantity
                print(f"** {quantity} order of {order_input} have been added to your meal **")
                return
    print(f"** Sorry '{order_input}' does not exists in Menu **")


if __name__ == "__main__":
    print(dedent(welcome_text))    
    print_menuitems()
    order = input(dedent(order_text))
    while order.lower() != "quit":
        take_order_details(order.lower())
        order = input(dedent(order_text))