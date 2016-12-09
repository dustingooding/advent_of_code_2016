#!/usr/bin/env python

import re

class Screen:
    def __init__(self, rows=1, columns=1):
        self.rows = rows
        self.columns = columns
        self.data = ['.'] * (self.rows * self.columns)

    def rect(self, a, b):
        for row in range(b):
            self.data[row * self.columns : row * self.columns + a] = '#' * (a)

    def rotate_row(self, a, b):
        for i in range(b):
            self.data[a * self.columns : a * self.columns + self.columns] = self._shift(self.data[a * self.columns : a * self.columns + self.columns])

    def rotate_column(self, a, b):
        for i in range(b):
            self.data[a : self.rows * self.columns : self.columns] = self._shift(self.data[a : self.rows * self.columns : self.columns])

    def lit_pixel_count(self):
        return self.data.count('#')

    def _shift(self, values):
        end = values[-1]
        values[1:] = values[:-1]
        values[0] = end
        return values

    def __str__(self):
        output = ''
        for row in range(self.rows):
            output += '['
            output += ''.join(self.data[row * self.columns : row * self.columns + self.columns])
            output += ']\n'
        return output

with open('input') as f:
    input_data = f.read()

# part 1
rect_cmd = re.compile(r"rect ([0-9]+)x([0-9]+)")
rotate_row_cmd = re.compile(r"rotate row y=([0-9]+) by ([0-9]+)")
rotate_column_cmd = re.compile(r"rotate column x=([0-9]+) by ([0-9]+)")

s = Screen(6, 50)
for cmd in input_data.split('\n'):
    rect_match = rect_cmd.match(cmd)
    if rect_match is not None:
        s.rect(int(rect_match.group(1)), int(rect_match.group(2)))
    else:
        rotate_row_match = rotate_row_cmd.match(cmd)
        if rotate_row_match is not None:
            s.rotate_row(int(rotate_row_match.group(1)), int(rotate_row_match.group(2)))
        else:
            rotate_column_match = rotate_column_cmd.match(cmd)
            if rotate_column_match is not None:
                s.rotate_column(int(rotate_column_match.group(1)), int(rotate_column_match.group(2)))
print 'part 1:', s.lit_pixel_count()

# part 2
print 'part 2:'
print s