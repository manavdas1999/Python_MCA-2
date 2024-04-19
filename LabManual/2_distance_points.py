#Q2. Write a program to compute distance between two points taking input from the user.

import math

x1, y1 = input("Enter x and y coordinate of point1 (comma separated): ").split(",")
x2, y2 = input("Enter x and y coordinate of point2 (comma separated): ").split(",")

# convert to suitable format
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
print(f"Distance between Point1 ({x1},{y1}) and Point2 ({x2},{y2}):", round(distance,2))
