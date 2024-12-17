"""Code to solve part 02 of day 13"""
import re
import sympy as sp


def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip())
    return all_lines

# def is_integer(number):
#     return np.isclose(number, np.round(number))

count = 1
button_a = None
button_b = None
prize = None
file = read_file('input')
total_tokens = 0

for line in file:
    a, b = sp.symbols('a b')
    if count == 1:
        numbers = re.findall(r'\d+', line)
        button_a = {"x": int(numbers[0]), "y": int(numbers[1])}
    elif count == 2:
        numbers = re.findall(r'\d+', line)
        button_b = {"x": int(numbers[0]), "y": int(numbers[1])}
    elif count == 3:
        numbers = re.findall(r'\d+', line)
        prize = {"x":   10000000000000 + int(numbers[0]), "y":  10000000000000 + int(numbers[1])}

        eq1 = sp.Eq(a * button_a["x"] + button_b["x"] * b, prize["x"])
        eq2 = sp.Eq(button_a["y"] * a + button_b["y"] * b, prize["y"])

        solution = sp.solve((eq1, eq2), (a, b))
        if solution[a].is_integer and solution[b].is_integer:
             total_tokens += ((3 * solution[a]) + solution[b])
    else:
        None
    count = count + 1 if count < 4 else 1

print(total_tokens)


