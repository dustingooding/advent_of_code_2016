#!/usr/bin/env python

class Keypad:
    def __init__(self, keys = [1], initial_row = 0, initial_column = 0):
        self.keys = keys
        self.rows = len(keys)
        self.columns = len(keys[0])
        self.current_row = initial_row
        self.current_column = initial_column

    def up(self):
        if self.current_row > 0:
            if self.keys[self.current_row - 1][self.current_column] is not None:
                self.current_row -= 1

    def down(self):
        if self.current_row < self.rows - 1:
            if self.keys[self.current_row + 1][self.current_column] is not None:
                self.current_row += 1

    def left(self):
        if self.current_column > 0:
            if self.keys[self.current_row ][self.current_column - 1] is not None:
                self.current_column -= 1

    def right(self):
        if self.current_column < self.columns - 1:
            if self.keys[self.current_row ][self.current_column + 1] is not None:
                self.current_column += 1

    def current_key(self):
        return keys[self.current_row][self.current_column]

with open('input') as f:
    input_data = f.read()

# Part 1

keys = [ [1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9] ]
keypad = Keypad(keys, 1, 1)
code = ''

for step in input_data.split('\n'):
    for move in step.strip():
        if move == 'U':
            keypad.up()
        if move == 'D':
            keypad.down()
        if move == 'L':
            keypad.left()
        if move == 'R':
            keypad.right()
    code += str(keypad.current_key())

print 'part 1:', code

# Part 2

keys = [ [None, None, '1', None, None], 
         [None, '2', '3', '4', None], 
         ['5', '6', '7', '8', '9'], 
         [None, 'A', 'B', 'C', None], 
         [None, None, 'D', None, None]]
keypad = Keypad(keys, 2, 0)
code = ''

for step in input_data.split('\n'):
    for move in step.strip():
        if move == 'U':
            keypad.up()
        if move == 'D':
            keypad.down()
        if move == 'L':
            keypad.left()
        if move == 'R':
            keypad.right()
    code += str(keypad.current_key())

print 'part 2:', code