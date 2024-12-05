"""Code to solve part 01 of day 05"""
from enum import Enum
import re

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

def is_valid_update(update1, rules):
    for page in update1:
        if not is_valid_page(page, update1, rules):
            return False
    return True

def get_applicable_rules(update1, rules):
    applicable_rules = list()
    for rule in rules:
        rule_pages = rule.split("|")
        if rule_pages[0] in update1 and rule_pages[1] in update1:
            applicable_rules.append(rule)
    return applicable_rules

def find_left_bound(rule_set):
    for rule in rule_set:
        candidate =  rule.split("|")[0]
        if len([r for r in rule_set if '|' + candidate in r]) == 0:
            return int(candidate)

def find_right_bound(rule_set):
    for rule in rule_set:
        candidate = rule.split("|")[1]
        if len([r for r in rule_set if candidate + '|' in r]) == 0:
            return int(candidate)


def fix(applicable_rules):
    left_bounds = list()
    right_bounds = list()
    while(len(applicable_rules)):
        left = find_left_bound(applicable_rules)
        right = find_right_bound(applicable_rules)
        left_bounds.append(left)
        right_bounds.insert(0,right)
        applicable_rules = [x for x in applicable_rules if str(left) not in x]
        applicable_rules = [x for x in applicable_rules if str(right) not in x]

    return left_bounds + right_bounds

ordering_rules = read_file('input_ordering_rules')
updates = read_file('input_updates')

RESULT = 0
for update in updates:
    update_pages = update.split(",")
    if len(update_pages) % 2 == 0:
        raise Exception("No middle could be found")
    if not is_valid_update(update_pages, ordering_rules):
        fixed_update = fix(get_applicable_rules(update, ordering_rules))
        middle = int([page for page in update_pages if int(page) not in fixed_update][0])
        RESULT += middle

print(RESULT)