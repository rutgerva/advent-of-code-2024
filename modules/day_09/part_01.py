"""Code to solve part 01 of day 08"""
from enum import Enum

class Mode(Enum):
    FREE_SPACE = 1
    FILE = 2
def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip())
    return all_lines

def swap_mode(current_mode):
    return Mode.FREE_SPACE if current_mode == Mode.FILE else Mode.FILE

dense_format = read_file('input')[0]

ID = 0
mode = Mode.FILE
disk_map = list()
for digit in dense_format:
    for i in range(0, int(digit)):
        if mode == Mode.FILE:
            disk_map.append(str(ID))
        else:
            disk_map.append('.')
    if mode == Mode.FILE:
        ID += 1
    mode = swap_mode(mode)
#fragment
latest_free_block = 0
for block_index in range(len(disk_map)-1, -1 , -1):
    if not disk_map[block_index] == '.' and len([x for x in range(0, block_index) if disk_map[x] == '.']) > 0:
        block = disk_map[block_index]
        for i in range(latest_free_block, len(disk_map)):
            if disk_map[i] == '.':
                disk_map[i] = block
                disk_map[block_index] = '.'
                latest_free_block = i
                break
# calculate checksum
index = 0
print(sum([block_index * int(disk_map[block_index]) for block_index in range(0, len(disk_map)) if disk_map[block_index] != '.']))

