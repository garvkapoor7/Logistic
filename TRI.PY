side1 = float(input("Enter length of 1st side = "))
side2 = float(input("Enter length of 2rd side = "))
side3 = float(input("Enter length of 3rd side = "))

if side1==0 or side2==0 or side3==0:
    print("Triangle side can't be zero")
elif (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)>side2:
    print("Triangle is possible")

else:
    print("Triangle is not possible")