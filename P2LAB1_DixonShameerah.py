# Shameerah Dixon
# April 12, 2026
# p2lab1.py
# Writing codes that perfom mathematical calculations

import math

# Get radius input from user and convert to a float
radius = float(input("What is the radius of the circle?: "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

#Display results
print (f"Diameter: {diameter:.2f}")
print (f"Circumference: {circumference:.2f}")
print (f"Area: {area:.2f}")