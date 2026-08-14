totalAmount=0
age1=int(input("enter the age of 1st person="))
tkp1=float(input("Enter the price of 1st person="))

if age1>12:
  disco=tkp1*(30/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount=(tkp1-disco)
elif age1>59:
  disco=tkp1*(50/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount+(tkp1-disco)
else:
  totalAmount=totalAmount+tkp1
print(totalAmount)

age2=int(input("enter the age of 2st person="))
tkp2=float(input("Enter the price of 2st person="))

if age2>12:
  disco=tkp2*(30/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount=(tkp2-disco)
elif age2>59:
  disco=tkp2*(50/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount+(tkp2-disco)
else:
  totalAmount=totalAmount+tkp2
print(totalAmount)

age3=int(input("enter the age of 3rd person="))
tkp3=float(input("Enter the price of 3rd person="))

if age3>12:
  disco=tkp3*(30/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount=(tkp3-disco)
elif age3>59:
  disco=tkp3*(50/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount+(tkp3-disco)
else:
  totalAmount=totalAmount+tkp3
print(totalAmount)

age4=int(input("enter the age of 4th person="))
tkp4=float(input("Enter the price of 4th person="))

if age4>12:
  disco=tkp4*(30/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount=(tkp4-disco)
elif age4>59:
  disco=tkp4*(50/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount+(tkp4-disco)
else:
  totalAmount=totalAmount+tkp4
print(totalAmount)

age5 = int(input("enter the age of 5th person="))
tkp5 = float(input("Enter the price of 5th person="))

if age5>12:
  disco = tkp5*(30/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount=totalAmount = (tkp5-disco)
elif age5>59:
  disco=tkp5*(50/100)
  print(f"Pasenger get discount of rs(disco)")
  totalAmount = totalAmount + (tkp5-disco)
else:
  totalAmount = totalAmount + tkp5
print(totalAmount)