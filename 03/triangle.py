#!/usr/bin/env python

class Triangle():
    def __init__(self, sides = [3, 4, 5]):
        self.sides = sides

    def valid(self):
        return ((self.sides[0] + self.sides[1] > self.sides[2]) and
                (self.sides[1] + self.sides[2] > self.sides[0]) and
                (self.sides[2] + self.sides[0] > self.sides[1]))


with open('input') as f:
    content = f.readlines()

# Part 1

valid_triangles = 0
content = [x.strip() for x in content]
for entry in content:
    sides = [int(x) for x in entry.split()]
    triangle = Triangle(sides)
    if triangle.valid():
        valid_triangles += 1

print 'part 1:', valid_triangles

# Part 2

valid_triangles = 0
content = [x.strip() for x in content]
for row in range(0,len(content),3):
    entry_0 = [int(x) for x in content[row].split()]
    entry_1 = [int(x) for x in content[row+1].split()]
    entry_2 = [int(x) for x in content[row+2].split()]
    triangle_0 = Triangle([entry_0[0], entry_1[0], entry_2[0]])
    triangle_1 = Triangle([entry_0[1], entry_1[1], entry_2[1]])
    triangle_2 = Triangle([entry_0[2], entry_1[2], entry_2[2]])
    if triangle_0.valid():
        valid_triangles += 1
    if triangle_1.valid():
        valid_triangles += 1
    if triangle_2.valid():
        valid_triangles += 1

print 'part 2:', valid_triangles