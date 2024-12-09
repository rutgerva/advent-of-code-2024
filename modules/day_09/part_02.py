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

def find_fitting_spot(d_map, length, max_index):
    count = 0
    index = 0
    for i in range(d_map.index('.'), len(d_map)):
        if i >= max_index:
            return -1
        if d_map[i] == '.':
            count += 1
            index = i if index == 0 else index
            if count == length:
                return index
        else:
            count = 0
            index = 0
    return -1


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
# print(disk_map)
ID -= 1
#fragment
block_length = 0
for block_index in range(len(disk_map) - 1, -1 , -1):
    if ID == 0:
        break
    if not disk_map[block_index] == '.' and disk_map[block_index] == str(ID):
        block_length += 1
    elif block_length != 0 and (disk_map[block_index] == '.' or int(disk_map[block_index]) != ID):
        from_index = find_fitting_spot(disk_map, block_length,block_index + 1)
        to_index = from_index + block_length - 1
        if from_index != -1:
            #replace
            disk_map = disk_map[0:from_index] + [str(ID) for x in range(0, block_length)] + disk_map[to_index + 1:]
            #replace spot of file
            for i in range(block_index + 1, block_index + block_length + 1):
                disk_map[i] = '.'
        # print(disk_map)
        ID -= 1
        block_length = 1 if disk_map[block_index] == str(ID) else 0

#calculate checksum
print(sum([block_index * int(disk_map[block_index]) for block_index in range(0, len(disk_map)) if disk_map[block_index] != '.']))

