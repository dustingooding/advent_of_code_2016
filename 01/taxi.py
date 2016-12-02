#!/usr/bin/env python

import copy


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

# class representing an intersection
class Intersection:
    # class constructor with default argument values
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return 'x={} y={}'.format(self.x, self.y)


# class representing a Taxi that keeps track of position and heading
class Taxi:
    # class constructor with default argument values
    def __init__(self, intersection = Intersection(), heading = Directions.N):
        self.start_intersection = intersection
        self.intersection = copy.deepcopy(self.start_intersection)
        self.heading = heading

    def turn_right(self):
        self.heading = Directions.turn_right(self.heading)

    def turn_left(self):
        self.heading = Directions.turn_left(self.heading)

    def drive(self, distance):
        if self.heading == Directions.N:
            self.intersection.x += distance
        elif self.heading == Directions.E:
            self.intersection.y += distance
        elif self.heading == Directions.S:
            self.intersection.x -= distance
        elif self.heading == Directions.W:
            self.intersection.y -= distance

    def blocks_from_start(self):
        return abs(self.start_intersection.x - self.intersection.x) + abs(self.start_intersection.y - self.intersection.y)

    def __str__(self):
        return 'taxi({} h={} b={})'.format(self.intersection, self.heading, self.blocks_from_start())



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

# Part 1
taxi = Taxi()

# split up instruction list into individual comma-separated steps
for step in instructions.split(', '):
    # python slice notation to get first character in the step
    if step[0:1] == 'R':
        taxi.turn_right()
    elif step[0:1] == 'L':
        taxi.turn_left()

    # python slice notation to get everything past the first character in the step
    taxi.drive(int(step[1:]))

print 'Part 1 - blocks from start:', taxi.blocks_from_start()

# Part 2
taxi = Taxi()

# create list of visited intersections, with current location as only entry
intersections = [ taxi.intersection ]
hq_intersection = None

# split up instruction list into individual comma-separated steps
for step in instructions.split(', '):
    # track beginning of step
    begin_intersection = copy.deepcopy(taxi.intersection)
    # python slice notation to get first character in the step
    if step[0:1] == 'R':
        taxi.turn_right()
    elif step[0:1] == 'L':
        taxi.turn_left()
    # python slice notation to get everything past the first character in the step
    taxi.drive(int(step[1:]))
    # track end of step
    end_intersection = copy.deepcopy(taxi.intersection)

    # if step's x is constant (East-West movement)
    if (begin_intersection.x == end_intersection.x):
        # find direction of travel
        if (begin_intersection.y < end_intersection.y):
            y_direction = 1
        else:
            y_direction = -1
        # generate all intersection between beginning and end of step
        for mid_y in range(begin_intersection.y, end_intersection.y, y_direction):
            mid_intersection = Intersection(begin_intersection.x, mid_y)
            # check for previous visit to current "mid" intersection
            if mid_intersection in intersections:
                # found
                hq_intersection = mid_intersection
                break
            else:
                # add to list
                intersections.append(mid_intersection)
    # if step's y is constant (North-South movement)
    elif (begin_intersection.y == end_intersection.y):
        # find direction of travel
        if (begin_intersection.x < end_intersection.x):
            x_direction = 1
        else:
            x_direction = -1
        # generate all intersection between beginning and end of step
        for mid_x in range(begin_intersection.x, end_intersection.x, x_direction):
            mid_intersection = Intersection(mid_x, begin_intersection.y)
            # check for previous visit to current "mid" intersection
            if mid_intersection in intersections:
                # found
                hq_intersection = mid_intersection
                break
            else:
                # add to list
                intersections.append(mid_intersection)

    # if hq intersection was found, don't go to next step
    if hq_intersection is not None:
        break

# teleport taxi (so you can math easier)
taxi.intersection = hq_intersection
print 'Part 2 - blocks from start:', taxi.blocks_from_start()
