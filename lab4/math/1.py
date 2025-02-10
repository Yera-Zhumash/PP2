#Write a Python program to convert degree to radian.

import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 15
radian = degree_to_radian(degree)

print("Input degree:", degree)
print("Output radian:", round(radian, 6))
