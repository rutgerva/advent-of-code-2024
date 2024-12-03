"""Code to solve part 02 of day 03"""
import re
def process_memory(memory_string):
    pattern = r"\w*mul\((-?\d*),(-?\d*)\)"
    matches = re.findall(pattern, memory_string)
    mem_result = 0
    for match in matches:
        mem_result += (int(match[0]) * int(match[1]))
    return mem_result

#Start in enabled state
enabled = True
#Read Memory
with open('input') as file:
    memory = file.read()
out_of_memory = False
RESULT = 0
while not out_of_memory:
    index = memory.find("don't()") if enabled else memory.find("do()")
    if index != -1:
        substr = memory[0:index]
        index  = index + 7 if enabled else index + 4
        memory = memory[index:len(memory)]
        if enabled:
            RESULT += process_memory(substr)
        enabled = not enabled
    else:
        if enabled:
            RESULT += process_memory(memory)
        out_of_memory = True

print(RESULT)
