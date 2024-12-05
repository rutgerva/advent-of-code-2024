"""Code to solve part 01 of day 05"""
from enum import Enum

class RULE_CONDITION(Enum):
    BEFORE = 1
    AFTER = 2

def read_file(filename):
    """Methods reads a file and returns stream of lines"""
    all_lines = []
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            all_lines.append(line.strip())
    return all_lines

def is_valid_page(page, all_pages, rules):
    for rule in rules:
        rule_pages = rule.split("|")
        other_page = rule_pages[1] if rule_pages[0] == page else rule_pages[0]
        if str(page) in rule and str(other_page) in all_pages:
            condition = RULE_CONDITION.BEFORE if rule_pages[0] == page else RULE_CONDITION.AFTER
            if (condition == RULE_CONDITION.BEFORE and all_pages.index(page) > all_pages.index(other_page)) or (condition == RULE_CONDITION.AFTER and all_pages.index(page) < all_pages.index(other_page)):
                return False
    return True

def is_valid_update(update, rules):
    for page in update:
        if not is_valid_page(page, update, rules):
            return False
    return True

ordering_rules = read_file('input_ordering_rules')
updates = read_file('input_updates')
RESULT = 0
for update in updates:
    update_pages = update.split(",")
    if len(update_pages) % 2 == 0:
        raise Exception("No middle could be found")
    middle = int(update_pages[int(len(update_pages) / 2)])
    if is_valid_update(update_pages, ordering_rules):
        RESULT += middle

print(RESULT)