# python program to Convert Days into Years, Weeks and Days
days = int(input("Enter number od days : "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
remaining_days = remaining_days % 7

print("Years =", years)
print("Weeks =",weeks)
print("Days =", remaining_days)
