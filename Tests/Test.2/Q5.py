p1 = int(input("Enter price 1: "))
p2 = int(input("Enter price 2: "))
p3 = int(input("Enter price 3: "))
p4 = int(input("Enter price 4: "))
p5 = int(input("Enter price 5: "))

total = p1 + p2 + p3 + p4 + p5
gst = total * 18 // 100
bill = total + gst

print("Total Bill =", bill)