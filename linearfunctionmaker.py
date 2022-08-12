import math

x1 = int(input("Point 1, x = "))
y1 = int(input("Point 1, y = "))
x2 = int(input("Point 2, x = "))
y2 = int(input("Point 2, y = "))

m = (y2-y1)/(x2-x1)
b = y1 - m*x1

print("y = " + str(m) + "x" + " + " + str(b))

