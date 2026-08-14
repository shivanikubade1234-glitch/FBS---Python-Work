# Write a program to canvert days into years, weeks and days
days = 1000
years = days // 365
print(years)
days = days % 365
print(days)

weeks =days //  7
print(weeks)
days = days % 7
print(days)
print(f'years:{years}, weeks:{weeks}, days:{days}.')