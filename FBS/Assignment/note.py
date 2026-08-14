amount = int(input("Enter the amount = "))

no2000 = amount // 2000
amount = amount % 2000

no500 = amount // 500
amount = amount % 500

no100 = amount // 100
amount = amount % 100

no50 = amount // 50
amount = amount % 50


no20 = amount // 20
amount = amount % 20


no10 = amount // 10
amount = amount % 10

print(f"fuzi amount ghari nenya sathi 2000{no2000} 500{no500} 100{no100} 50{no50} 20{no20} 10{no10}")