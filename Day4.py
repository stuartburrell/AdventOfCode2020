with open('inputd4.txt') as f:
    inputs = [x for x in f]

processed = ['']
index = 0
for x in inputs:
    if x == '\n':
        processed.append('')
        index += 1
    else:
        processed[index] += x

# Part 1
        
def valid_check1(string):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for f in fields:
        if f not in string:
            return False
    return True       
    
total_valid1 = 0
p1valid = [] 
for s in processed:
    if valid_check1(s):
        total_valid1 += 1
        p1valid.append(s)
print('Part 1: ', total_valid1)

# Part 2

def year_check(string, lower, upper):
    if len(string) != 4:
        return False
    yr = int(string)
    if yr >= lower and yr <= upper:
        return True
    return False

def height_check(string):
    if string[-2:] == 'cm':
        ht = int(string[:-2])
        if ht >= 150 and ht <= 193:
            return True
    elif string[-2:] == 'in':
        ht = int(string[:-2])
        if ht >= 59 and ht <= 76:
            return True
    return False

def hcol_check(string):
    if string[0] != '#':
        return False
    if len(string[1:]) != 6:
        return False
    valid = [str(x) for x in range(10)] + ['a','b','c','d','e','f']
    for char in string[1:]:
        if char not in valid:
            return False
    return True

def ecol_check(string):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if string not in valid:
        return False
    return True

def pass_check(string):
    if len(string) != 9:
        return False
    valid = [str(x) for x in range(10)]
    for char in string:
        if char not in valid:
            return False
    return True

def valid_check2(string):
    s = string.replace(' ', '\n').split('\n')[0:-1]
    for entry in s: 
        code, value_str = entry.split(':')[0], entry.split(':')[1]
        if code == 'byr' and not year_check(value_str, 1920, 2002):
            return False   
        if code == 'iyr' and not year_check(value_str, 2010, 2020):
            return False   
        if code == 'eyr' and not year_check(value_str, 2020, 2030):
            return False 
        if code == 'hgt' and not height_check(value_str):
            return False
        if code == 'hcl' and not hcol_check(value_str):
            return False 
        if code == 'ecl' and not ecol_check(value_str):
            return False
        if code == 'pid' and not pass_check(value_str):
            return False
    return True

total_valid2 = 0
for string in p1valid:
    if valid_check2(string):
        total_valid2 += 1
print('Part 2: ', total_valid2)