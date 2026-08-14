# Python Program to Calculate Compound Interest
p = int(input('Enter amount of principle:'))
r = int(input('Enter rate of interest:'))
t = int(input('Enter time:'))

ci = p * (1 + r/100)**t-p

print("compound interset =", ci)