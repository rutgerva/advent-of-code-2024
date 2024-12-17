"""Code to solve part 01 of day 14"""
import re

GRID_HEIGHT = 103
GRID_WIDTH = 101

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip())
    return all_lines

def move(robot):
    new_x =  (robot["p_x"] + robot["v_x"]) % GRID_WIDTH
    new_y =  (robot["p_y"] + robot["v_y"]) % GRID_HEIGHT
    return {
        "p_x": new_x, "p_y": new_y, "v_x": robot["v_x"], "v_y": robot["v_y"]
    }

def in_quadrant(robot):
    if robot["p_x"] < GRID_WIDTH // 2:
        if robot["p_y"] < GRID_HEIGHT // 2:
            return 0
        elif GRID_HEIGHT // 2 < robot["p_y"] < GRID_HEIGHT:
            return 3
        else:
            return 4
    elif GRID_WIDTH // 2 < robot["p_x"] < GRID_WIDTH:
        if robot["p_y"] < GRID_HEIGHT // 2:
            return 1
        elif GRID_HEIGHT // 2 < robot["p_y"] < GRID_HEIGHT:
            return 2
        else:
            return 4
    else:
        return 4

def init_robots():
    robots = list()
    for robot in robot_list:
        coordinates = re.findall(r'-?\d+', robot)
        r = { "p_x" : int(coordinates[0]),"p_y" : int(coordinates[1]),"v_x" : int(coordinates[2]),"v_y" : int(coordinates[3])}
        robots.append(r)
    return robots

robot_list = read_file('input')

init_robots()
robots = init_robots()

robots_per_quadrant = [0 , 0 , 0 , 0 , 0] # last index is the bucket of robots on a horizontal and/or veritcal axis between quadrants
# after_move = list()
for r in robots:
    for i in range(0, 100):
        r = move(r)
    # after_move.append(r)
    robots_per_quadrant[in_quadrant(r)] += 1

print(robots_per_quadrant[0] * robots_per_quadrant[1] * robots_per_quadrant[2] * robots_per_quadrant[3])


