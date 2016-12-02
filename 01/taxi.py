#!/usr/bin/env python

# class representing a Direction enum (Python2 doesn't have enums)
class Directions:
    N, E, S, W = range(4)

    # clockwise moves right (positive) through the enum
    @staticmethod
    def turn_right(initial_heading):
        return Directions._normalize((initial_heading + 1), Directions.N, Directions.W+1)

    # counter-clockwise moves left (negative) through the enum
    @staticmethod
    def turn_left(initial_heading):
        return Directions._normalize((initial_heading - 1), Directions.N, Directions.W+1)

    # method for "wrapping" the directions around the enum edges
    @staticmethod
    def _normalize(value, min, max):
        normalized = value
        range = max - min
        while (normalized < min):
            normalized += range
        while (normalized >= max):
            normalized -= range
        return normalized

# class representing a Taxi that keeps track of position and heading
class Taxi:
    # class constructor with default argument values
    def __init__(self, x = 0, y = 0, heading = Directions.N):
        # multi-assignment of class member variables
        self.x = self.start_x = x
        self.y = self.start_y = y
        self.heading = heading

    def turn_right(self):
        self.heading = Directions.turn_right(self.heading)

    def turn_left(self):
        self.heading = Directions.turn_left(self.heading)

    def drive(self, distance):
        if self.heading == Directions.N:
            self.x += distance
        elif self.heading == Directions.E:
            self.y += distance
        elif self.heading == Directions.S:
            self.x -= distance
        elif self.heading == Directions.W:
            self.y -= distance

    def blocks_from_start(self):
        return abs(self.start_x - self.x) + abs(self.start_y - self.y)

    # Python's `print` command uses the __str__() method to display a class
    def __str__(self):
        return 'taxi(x={} y={} h={} b={})'.format(self.x, self.y, self.heading, self.blocks_from_start())




taxi = Taxi()

# multiline string syntax
instructions = ('L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, '
                'L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, '
                'R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, '
                'R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, '
                'L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, '
                'R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, '
                'L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, '
                'R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, '
                'R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, '
                'R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, '
                'L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5')

# split up instruction list into individual comma-separated steps
for step in instructions.split(', '):
    # python slice notation to get first character in the step
    if step[0:1] == 'R':
        taxi.turn_right()
    elif step[0:1] == 'L':
        taxi.turn_left()
    # python slice notation to get everything past the first character in the step
    taxi.drive(int(step[1:]))

print taxi
