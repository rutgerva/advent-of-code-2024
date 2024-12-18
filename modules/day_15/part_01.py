"""Code to solve part 01 of day 15"""
import numpy as np

ROBOT_POS = {}

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append([c for c in line.strip()])
    return all_lines

def read_file_controls(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines += [c for c in line.strip()]
    return all_lines

def valid_spot(row, col, grid):
    return len(grid) > row > 0 and len(grid[row]) > col > 0 and grid[row][col] != '#'

def can_move(row, col, drow, dcol, grid):
    if valid_spot(row, col , grid):
        if grid[row][col] == '.':
            return True
        else:
            return can_move(row + drow, col + dcol, drow, dcol, grid)
    else:
        return False

def move_item(row, col, drow, dcol, grid, current_symbol):
    if grid[row + drow][col + dcol] != '.':
        move_item(row + drow, col + dcol, drow, dcol, grid, grid[row + drow][col + dcol])
    grid[row + drow][col + dcol] = current_symbol


def move(instruction, grid):
    delta_row = 0
    delta_col = 0
    global ROBOT_POS
    if instruction == '<':
        delta_col = -1
    elif instruction == '^':
        delta_row = -1
    elif instruction == 'v':
        delta_row = 1
    elif instruction == '>':
        delta_col = 1
    else:
        raise Exception("No valid instruction received")
    if can_move(ROBOT_POS["row"], ROBOT_POS["col"], delta_row, delta_col, grid):
        row = ROBOT_POS["row"]
        col = ROBOT_POS["col"]
        ROBOT_POS["row"] += delta_row
        ROBOT_POS["col"] += delta_col
        grid[row][col] = '.'
        move_item(row, col, delta_row, delta_col, grid, '@')


def find_sum_of_coordinates(grid):
    sum = 0
    for i, row in enumerate(grid, 0):
        for j, col in enumerate(row, 0):
            if grid[i][j] == 'O':
                sum += (100 * i) + j
    return sum


def init(grid):
    global ROBOT_POS
    for i, row in enumerate(grid, 0):
        for j, col in enumerate(grid[i], 0):
            if grid[i][j] == '@':
                ROBOT_POS = {"row": i, "col":j}

warehouse = np.array(read_file('input_map'))
instructions = read_file_controls('input_controls')
init(warehouse)
print(instructions)
for instruction in instructions:
    move(instruction, warehouse)

print(warehouse)
print(find_sum_of_coordinates(warehouse))

