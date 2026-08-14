def area(length,breadth):

    area = length * breadth

    return(area)

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

res = area(length,breadth)
print('area of rectangle: ', res)