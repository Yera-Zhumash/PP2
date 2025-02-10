#Write a Python program to calculate the area of regular polygon.
import math

def regular_polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

sides = 4
length = 25
area = regular_polygon_area(sides, length)

print("Input number of sides:", sides)
print("Input the length of a side:", length)
print("The area of the polygon is:", round(area, 1))
