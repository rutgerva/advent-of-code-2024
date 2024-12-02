"""Code to solve part 01 of day 01"""
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
#Sort columns
col1.sort()
col2.sort()

RESULT = 0

for i in range(len(col1)):
    RESULT += abs(col1[i] - col2[i])

print(RESULT)

