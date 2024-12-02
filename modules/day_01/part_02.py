"""Code to solve part 02 of day 01"""
import re
def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line)
    return all_lines
#Read file
lines = read_file('input')
col1 = []
col2 = []
#Fetch numbers
for line in lines:
    print(line)
    lineNumbers = re.split('\s+', line)
    col1.append(int(lineNumbers[0]))
    col2.append(int(lineNumbers[1]))
RESULT = 0

for location in col1:
    RESULT+= location * col2.count(location)
print(RESULT)
