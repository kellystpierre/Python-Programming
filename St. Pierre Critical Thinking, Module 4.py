# Kelly St. Pierre
# CSC500-1
# Critical Thinking, Module 4

# Step 1: Create ItemToPurchase class

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(self.item_name, self.item_quantity, "@ $", self.item_price, "= $", total)

# Step 2: Prompt for two items and create two objects

print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Enter item name: ")
item1.item_price = int(input("Enter item price: $"))
item1.item_quantity = int(input("Enter item quantity: "))

print("Item 2")
item2 = ItemToPurchase()
item2.item_name = input("Enter item name: ")
item2.item_price = int(input("Enter item price: $"))
item2.item_quantity = int(input("Enter item quantity:"))

# Step 3: Add the costs of two items and output cost

print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print("Total: $", total_cost)
