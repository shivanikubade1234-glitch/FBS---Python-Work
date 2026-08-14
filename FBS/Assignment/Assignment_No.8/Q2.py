def area(radius):

    area = 3.14 * (radius**2)
    return area

radius= float(input("Enter radius: "))


res = area(radius)
print('area of circle: ', res)

