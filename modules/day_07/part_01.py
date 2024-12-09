"""Code to solve part 01 of day 07"""

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip())
    return all_lines

def construct_equation(operands, t_value, cur_total):
    #Stop condition 1 all operands used
    if len(operands) == 0:
        return cur_total == t_value
    #Stop condition 2: both options exceed Test value
    if cur_total * int(operands[0]) > t_value and cur_total + int(operands[0]) > t_value:
        return False
    #if multiply fails, then plus must hold
    if cur_total * int(operands[0]) > t_value:
        return construct_equation(operands[1:], t_value, cur_total + int(operands[0])) # Stop condition 3, only option left to create a valid equation from this point
    else:
        return construct_equation(operands[1:], t_value, cur_total * int(operands[0])) or construct_equation(operands[1:], t_value, cur_total + int(operands[0]))


def has_equation(operands, t_value):
    return construct_equation(operands[1:], t_value, int(operands[0]))

RESULT = 0
lines = read_file('input')
for line in lines:
    test_value = line.split(":")[0]
    equation_operands = list(line.split(":")[1].strip().split(" "))
    RESULT = RESULT + int(test_value) if has_equation(equation_operands, int(test_value)) else RESULT

print(RESULT)
