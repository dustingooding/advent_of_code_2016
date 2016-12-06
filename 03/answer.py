#!/usr/bin/env python

class Triangle():
    def __init__(self, sides = [3, 4, 5]):
        self.sides = sides

    def valid(self):
        return ((self.sides[0] + self.sides[1] > self.sides[2]) and
                (self.sides[1] + self.sides[2] > self.sides[0]) and
                (self.sides[2] + self.sides[0] > self.sides[1]))


with open('input') as f:
    input_data = f.readlines()
input_data_stripped = [x.strip() for x in input_data]

# Part 1

valid_triangles = 0
for entry in input_data_stripped:
    sides = [int(x) for x in entry.split()]
    triangle = Triangle(sides)
    if triangle.valid():
        valid_triangles += 1

print 'part 1:', valid_triangles

# Part 2

valid_triangles = 0
for row in range(0,len(input_data_stripped),3):
    entry_0 = [int(x) for x in input_data_stripped[row].split()]
    entry_1 = [int(x) for x in input_data_stripped[row+1].split()]
    entry_2 = [int(x) for x in input_data_stripped[row+2].split()]
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