# Kelly St. Pierre
# CSC500-1
# Critical Thinking, Module 5

# Part 1: Collect data and calculate average rainfall over a period of years

#initialize counting
total_rainfall = float()
total_months = 0

# Ask for number of years
years = int(input("Enter the number of years: "))

# Outer loop: per year; Inner loop: per month
for year in range(years):
    for month in range(12):
        month_rainfall = float(input("Enter rainfall for month: "))
        total_rainfall = total_rainfall + month_rainfall
        total_months = total_months + 1

average = total_rainfall / total_months

print("Total months: ", total_months)
print("Total rainfall: ", total_rainfall)
print("Average rainfall: ", average)

# Part 2: Calculate award poitns at CSU Global bookstore 

# Ask for number of books purchased
books_purchased = int(input("Number of books purchased this month: "))

# Arrange conditionals to caluculate points awarded
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0

print ("Points awarded: ", points)