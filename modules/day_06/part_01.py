"""Code to solve part 01 of day 06"""
import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(list(line.strip()))
    return all_lines

def turn_90_degrees(direction):
    if direction == Direction.LEFT:
        return Direction.UP
    else:
        return Direction(direction.value + 1)

def find_initial_position():
    possible_directions = [(Direction.UP, '^'), (Direction.RIGHT, '>'), (Direction.DOWN, 'v'), (Direction.LEFT, '<')]
    for direction in possible_directions:
        location = np.where(guard_map == direction[1])
        if len(location[0]) > 0:
            return direction[0], (int(location[0][0]), int(location[1][0]))

def has_object(row, column):
    matches = [True for i in range(0, len(objects[0])) if objects[0][i] == row and objects[1][i] == column]
    if len(matches) > 0:
        return True
    return False

def traverse(direction, from_location):
    #Same column, row index smaller than current location
    if direction == Direction.UP:
        for row in range(from_location[0], -1 , -1):
            if has_object(row, from_location[1]):
                return True, row + 1, from_location[1], Direction.RIGHT
            mark_position(row, from_location[1])
    # # same row, column index greater than current location
    elif direction == Direction.RIGHT:
        for col in range(from_location[1], len(guard_map[0])):
            if has_object(from_location[0], col):
                return True, from_location[0], col -1, Direction.DOWN
            mark_position(from_location[0], col)
    # # same column, row index greater than current location
    elif direction == Direction.DOWN:
        for row in range(from_location[0], len(guard_map[1])):
            if has_object(row, from_location[1]):
                return True, row - 1, from_location[1], Direction.LEFT
            mark_position(row, from_location[1])
    # # same row, column index smaller than current location
    else:
        for col in range(from_location[1], -1, -1):
            if has_object(from_location[0], col):
                return True, from_location[0], col + 1, Direction.UP
            mark_position(from_location[0], col)
    return False, None, None, None

def mark_position(row , col):
    guard_map[row][col] = 'X'

guard_map = np.array(read_file('input'))
current_direction, current_location = find_initial_position()
objects = np.where(guard_map == '#')
# print(current_direction)
# print(current_location)
# print(objects)
collision_detected = True
while collision_detected:
    result = traverse(current_direction, current_location)
    collision_detected = result[0]
    current_location = result[1], result[2]
    current_direction = result[3]
    # print(guard_map)
    # print(current_direction)
    # print(current_location)

print(len(np.where(guard_map == 'X')[0]))