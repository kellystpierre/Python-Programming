# Kelly St. Pierre
# CSC500-1
# Critical Thinking, Module 6

# Step 4: Build ShoppingCart class

class ItemToPurchase: #From previous assignment

    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

class ShoppingCart: 

    # Initialize customer name, date, and empty cart
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an item_to_purchase object
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Removes item by name
    def remove_item(self, item_name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")

    # Modifies existing item
    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:

                # Update description
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description

                # Update price
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
            
                # Update quantity
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
            
                return
        
        print("Item not found in cart. Nothing modified.")
    
    # Calculate total quantity of all items in cart
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    # Calculate total cost of all items in cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    # Print cart summary
    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items:", self.get_num_items_in_cart())

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        for item in self.cart_items:
            item_total = item.item_price * item.item_quantity
            print(item.item_name, item.item_quantity, "@ $", item.item_price, " = $", item_total)

        print ("Total: $", self.get_cost_of_cart())
    
    # Print item descriptions
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")

        for item in self.cart_items:
            print(item.item_name + ":", item.item_description)

# Step 5: Implement print_menu() function

def print_menu(cart):
    choice = ""

    while choice != "q":
        # Display menu
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        # Get user choice
        choice = input("Choose an option: ")

        # Validate input
        while choice not in ["a", "r", "c", "i", "o", "q"]:
            choice = input("Choose an option: ")
        
        if choice == "q":
            print("Exiting menu.")
            return
        
        elif choice == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = int(input("Enter the item price: $"))
            item_quantity = int(input("Enter the item quantity: "))

            item = ItemToPurchase(item_name, item_price, item_quantity)
            item.item_description = item_description
            cart.add_item(item)
        
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name) 
       
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))

            item = ItemToPurchase(item_name, 0, new_quantity)
            item.item_description = "none"
            cart.modify_item(item)
        
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

# Step 6: Implement Output shopping cart menu option. Implement Output item's description menu option.

def main():

    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    print()
    print("Customer name: ", customer_name)
    print("Today's date: ", current_date)
    print()

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)

main()

        