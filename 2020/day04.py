# Passport Processing

import re

def read_from_file(file_name):
    _file = open(file_name, "r")
    _read = _file.read()
    _file.close()
    return _read

valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
passports = read_from_file("inputs/day04.input").split("\n\n")

def solve1():
    global valid_keys
    global passports

    num_valid = 0
    for passport in passports:
        spassport = re.split('\s', passport)
        num_keys = 0
        for i in spassport:
            if i[0:3] in valid_keys:
                if i[0:3] != "cid":
                    num_keys+=1
        if num_keys == 7:
            num_valid +=1
    return num_valid

def solve2():
    global valid_keys
    global passports

    num_valid = 0
    for passport in passports:
        spassport = re.split('\s', passport)
        num_keys = 0
        for i in spassport:
            key = i[0:3]
            value =i[4:]
            prev_keys = num_keys
            if key == "byr":
                if int(value) >= 1920 and int(value) <= 2002:
                    num_keys += 1
            if key == "iyr":
                if int(value) >= 2010 and int(value) <= 2020:
                    num_keys += 1
            if key == "eyr":
                if int(value) >= 2020 and int(value) <= 2030:
                    num_keys += 1
            if key == "hgt":
                mt = value[-2:]
                if mt == "cm":
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        num_keys += 1
                if mt == "in":
                    if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        num_keys += 1
            if key == "hcl":
                hcl_pattern = re.compile("^#[\dabcdef]{6}")
                if hcl_pattern.search(value):
                    num_keys += 1
            if key == "ecl":
                ecl_pattern = re.compile("(amb|blu|brn|gry|grn|hzl|oth)")
                if ecl_pattern.search(value):
                    num_keys += 1
            if key == "pid":
                pid_pattern = re.compile("\d{9}")
                if pid_pattern.search(value):
                    if len(value) == 9:
                        num_keys += 1
            if key == 'cid':
                pass
        if num_keys == 7:
            num_valid +=1
    return num_valid

print("Pt1:", solve1())
print("Pt2:", solve2())
