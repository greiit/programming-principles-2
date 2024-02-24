#1
import math

def converting(degree):
    return degree * (math.pi / 180)

degree = int(input("Enter the degree: "))
radian = converting(degree)
print(f"Output radian: {radian}")

#2
import math

def area(height, base1, base2):
    return (base1 + base2) * height / 2
input_values = input("Enter the height and bases: ").split()
height, base1, base2 = [int(value) for value in input_values]

tarea = area(height, base1, base2)
print(tarea)

#3
import math

def polygon_area(sides, length):
    area = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
    return round(area)
input_values = input("Enter number of sides and length of a side: ").split()
sides, length = map(int, input_values)

parea = polygon_area(sides, length)
print(f"The area of the polygon is: {parea}") 

#4
import math

def parallelogram_area(length, height):
    return length * height
input_values = input("Enter the length and height: ").split()
length, height = [int(value) for value in input_values]

area = parallelogram_area(length, height)
print(f"The area of the parallelogram is: {round(area, 2)}")