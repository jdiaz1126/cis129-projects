#Josh Diaz, CIS129
#This section asks the user for the number of each item
print("Hello welcome to my coffee shop!")
num_coffees = int(input("Enter the number of coffees: "))
num_muffins = int(input("Enter the number of muffins: "))
num_bagels = int(input("Enter the number of bagels: "))
num_egg_sandwiches = int(input("Enter the number of egg sandwiches: "))
#This section is the price for each item
coffee_price = 5
muffin_price = 4
bagel_price = 6
egg_sandwich_price = 8
#This section calculates the subtotal, tax rate, tax amount, and total
subtotal = ((num_coffees + num_muffins + num_bagels + num_egg_sandwiches) * coffee_price)
tax_rate = 0.06
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
#This section prints out a receipt
print("===Receipt===")
print(f"Number of coffees: {num_coffees}")
print(f"Number of muffins: {num_muffins}")
print(f"Number of bagels: {num_bagels}")
print(f"Number of egg_sandwiches: {num_egg_sandwiches}")
#This section calculates the total
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
print("Thank you for shopping with us!")
