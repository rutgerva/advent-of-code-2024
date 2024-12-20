"""Code to solve part 01 of day 11"""
import getopt

import numpy as np

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append([c for c in line.strip()])
    return all_lines

def connects_to(x1, y1, x2, y2):
    # Calculate the differences in x and y coordinates
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    # Check if both differences are at most 1
    return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

def get_edges_from_area(area):
    edges = list()
    fences = 0
    for point in area:
        row = point[0]
        col = point[1]
        #check up
        if [row -1, col] not in area:
            edges += [{"point" : point, "dir": "HU"}]
        if [row, col + 1] not in area:
            edges += [{"point" : point, "dir": "VR"}]
        if [row + 1, col] not in area:
            edges += [{"point" : point, "dir": "HD"}]
        if [row, col - 1] not in area:
            edges += [{"point": point, "dir": "VL"}]

    return edges


def extract_area(row, col):
    element = field[row][col]
    area = list()
    area.append([row, col])
    field[row][col] = '.'
    hit_found = True
    while hit_found:
        hit_found = False
        r, c = np.nonzero(field == element)
        for i in range(0, len(r)):
            if any(connects_to(area[j][0], area[j][1], r[i], c[i]) for j in range(0, len(area))):
                area.append([r[i], c[i]])
                field[r[i]][c[i]] = '.'
                hit_found = True
    return area

def calculate_number_edges(edges):
    long_edges = 0
    edges = sorted(edges , key=lambda k: [k["point"][0], k["point"][1]])
    while(len(edges) > 0):
        edge = edges[0]
        direction = edge["dir"]
        curr_edge = list([edge["point"]])
        index = 1 if direction.startswith('V') else 0
        for other_edge in list.copy(edges[1:]):
            if (direction == other_edge["dir"]
                    and other_edge["point"] not in curr_edge
                    and other_edge["point"][index] == edge["point"][index]
                    and connects_to(other_edge["point"][1], other_edge["point"][0], curr_edge[-1][1], curr_edge[-1][0])):
                curr_edge.append(other_edge["point"])
                edges.remove(other_edge)
        edges.remove(edge)
        long_edges += 1
    return long_edges



field = np.array(read_file('input'))
def print_field():
    for row in field:
        for element in row:
            print(element, end="")
        print("")
    print("--------------------------------------------------------------------")

RESULT = 0
for row in range(0, len(field)):
    for col in range(0, len(field[row])):
        #print_field()
        if field[row][col] != '.':
            area = extract_area(row, col)
            edge_coordinates = get_edges_from_area(area)
            number_of_edges = calculate_number_edges(edge_coordinates)
            print(str(row) + ',' + str(col))
            print("perimeter = " + str(number_of_edges))
            print(len(area))
            print("\n")
            RESULT += (len(area) * number_of_edges)

print(RESULT)


