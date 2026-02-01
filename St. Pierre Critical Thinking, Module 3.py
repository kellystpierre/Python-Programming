# Kelly St. Pierre
# CSC500-1
# Critical Thinking, Module 3

#Part 1: Calculate meal tip, tax, and total

food_charge = float(input("Enter food charge: $"))

tip_amount = food_charge * 0.18
food_charge_incl_tip = food_charge + tip_amount

tax_amount = food_charge * 0.07
food_cost_incl_tax = food_charge + tax_amount

total_price = food_charge + tip_amount + tax_amount

print("Food charge with 18% gratuity: $", round(food_charge_incl_tip, 2))
print("Food charge with 7% sales tax: $", round(food_cost_incl_tax, 2))
print("Total cost, including gratuity and sales tax: $", round(total_price, 2))

#Part 2: Determine hour alarm will sound

current_time = int(input("Enter current time to nearest hour in 24 hour clock (0-23):"))

wait_time = int(input("Enter desired number of hours until alarm will sound:"))

alarm_time = (current_time + wait_time) % 24

print("Alarm will sound (in hours 0-23):", alarm_time)
