# Calculate selling price based on cost price and discount
cp = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = cp * discount / 100
sp = cp - discount_amount

print("Selling price =", sp)