"""
Name:
Date:
Description:
"""
import math

def slope(point1:tuple,point2:tuple)->float:
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    delta_y = abs(y2-y1)
    delta_x = abs(x2-x1)
    return delta_y/delta_x

def distance(point1:tuple, point2:tuple)->float:
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    delta_y = abs(y2 - y1)
    delta_x = abs(x2 - x1)
    dist = math.sqrt(delta_x**2+delta_y**2)
    return dist

def main():
    point1 = (1,2)
    point2 = (4,6)
    print(distance(point1,point2))

if __name__ == "__main__":
    main()