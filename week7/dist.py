import math

def distance1(x1, y1, x2, y2):
    return round(math.dist([x1, y1], [x2, y2]), 2)

def distance2(p1, p2):
    return round(math.dist(p1, p2), 2)

def distance3(c1, c2):
    overlap = False
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    
    d3 = round(math.dist([x1, y1], [x2, y2]), 2)
    if d3 - r1 - r2 <= 0:
        overlap = True
    return d3, overlap

def perimeter(points):
    perimeter = 0
    for i in range(len(points)):
        try:
            perimeter += math.dist(points[i], points[i + 1]) 
        except:
            perimeter += math.dist(points[i], points[0])
            return perimeter
        
exec(input().strip())