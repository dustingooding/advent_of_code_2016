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
