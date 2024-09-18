#!/usr/bin/env python3

print("The Area and Perimeter Of the Rectangle")
print()

length = float(input("length:\t"))
width = float(input("width:\t"))

area = length * width
perimeter = 2 * (length + width)

area = round(area, 3)
perimeter = round(perimeter, 3)

print()
print(f"Area:\t\t{area}")
print(f"Perimeter:\t{perimeter}")

