# Python program to calculate Simple Interest

# Take inputs from the user
P = int(input("Enter the Principal amount (P): "))
T = int(input("Enter the Time period in years (T): "))
R = int(input("Enter the Rate of interest (R): "))

# Calculate simple interest
SI = (P * T * R) / 100

# Display the calculated interest
print(f"\nThe Simple Interest is: {SI:.2f}")