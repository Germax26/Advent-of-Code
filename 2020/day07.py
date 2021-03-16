# Handy Haversack

import re

def read_from_file(file_name):
    _file = open(file_name, 'r')
    _read = _file.read()
    _file.close()
    return _read

def format_rules(rules_content):
    rules = []
    for rule in rules_content:
        srule = rule.split(" bags contain ")
        second_arg = [[x[:1], x[2:]] for x in re.split(" bags?,? ?", srule[1]) if x != "no other"][:-1]
        if len(second_arg) != 0:
            for i in second_arg:
                i[0] = int(i[0])
        rules.append([srule[0], second_arg])
    return rules

rules = format_rules(read_from_file('inputs/day07.input').split("\n"))
    
def solve1():
    final = []
    queue = ["shiny gold"]

    while queue != []:
        current = queue[0]
        final.append(current)
        queue.pop(0)

        # Go through all the rules, if that rules states that a 
        # bag must contain atleast one bag of the current colour,
        # append that bag's colour to the queue if it isn't already
        # in the queue or in the final list.

        for rule in rules:
            if current in [_rule[1] for _rule in rule[1]]:
                if rule[0] not in final[1:] and rule[0] not in queue:
                    queue.append(rule[0])
        
    return len(final[1:])

def num_inner(rules, colour):
    for rule in rules:
        if rule[0] == colour:
            return sum([bag[0] * (num_inner(rules, bag[1]) + 1) for bag in rule[1]])

def solve2():
    return num_inner(rules, 'shiny gold')

print("Pt1:", solve1())
print("Pt2:", solve2())
