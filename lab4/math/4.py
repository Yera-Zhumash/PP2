#Write a Python program to calculate the area of a parallelogram.
def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
area = parallelogram_area(base, height)

print("Length of base:", base)
print("Height of parallelogram:", height)
print("Expected Output:", float(area))
