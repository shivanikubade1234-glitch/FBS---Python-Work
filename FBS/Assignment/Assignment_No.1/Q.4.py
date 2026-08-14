#  python program to enter P, T, R and calculate simple Interest.

p = int(input('Enter amount of principle:'))
r = int(input('Enter rate of interest:'))
t = int(input('Enter time:'))

# perform operation
si = (p * r * t) / 100
print("Simple Interest =", si)