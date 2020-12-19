with open('data/inputd19.txt') as f:
    inputs = [x[0:-1] for x in f]
    
rules = {x.split(':')[0]:x.split(': ')[1] for x in inputs if ':' in x}
messages = [x for x in inputs if ': ' not in x][1:]

for key in rules:
    if '|' not in rules[key]:
        rules[key] = [[x for x in rules[key].split(' ')]]
    else:
        part1 = rules[key].split(' | ')[0]
        part2 = rules[key].split(' | ')[1]
        rules[key] = [[x for x in part1.split(' ')], [x for x in part2.split(' ')]]

rules_parsed = {}
for key in rules:
    if rules[key] == [['"a"']] or rules[key] == [['"b"']]:
        rules_parsed[key] = [rules[key][0][0][1]]

def update_parsed(key):
    test = all(all(x in rules_parsed.keys() for x in rules[key][i]) for i in range(len(rules[key])))
    if test:
        rules_parsed[key] = []
        for i in range(len(rules[key])):
            if len(rules[key][i]) == 2:
                for string1 in rules_parsed[rules[key][i][0]]:
                    for string2 in rules_parsed[rules[key][i][1]]:
                        rules_parsed[key].append(string1 + string2)
            elif len(rules[key][i]) == 1:
                for string1 in rules_parsed[rules[key][i][0]]:
                    rules_parsed[key].append(string1)

changed = True
while changed:
    old = rules_parsed.copy()
    for key in rules:
        update_parsed(key)
    if rules_parsed == old:
        changed = False

print('Part 1: ', sum([1 for m in messages if m in rules_parsed['0']]))

# Part 2

new_rules = rules.copy()
new_rules['8'] = [['42'], ['42', '8']]
new_rules['11'] = [['42', '31'], ['42', '11', '31']]

def test_message(string): 
    
    '''
    Valid messages are of the form 42*n + 31*k for n, k integers and k > n, 
    where 42 represents any message satisfying rule 42 and similarly for 31.
    All messages satisgying 42 or 31 have length 8.
    '''
    
    if len(string) % 8 != 0:
        return False
    elif string[0:8] not in rules_parsed['42']:
        return False
    elif string[-8:] not in rules_parsed['31']:
        return False
    else:
        num_42_blocks, num_31_blocks = 1, 1
        block = -8

    regime31 = True
    while regime31:
        if string[block - 8 : block] in rules_parsed['31']:
            block -= 8
            num_31_blocks += 1 
        elif string[block - 8 : block] in rules_parsed['42']:
            regime31 = False
        else:
            return False
        
    regime42 = True
    while regime42:
        if string[block - 8: block] not in rules_parsed['42']:
            return False
        else:
            num_42_blocks += 1
            block -= 8
        if block - 8 == -len(string) and num_42_blocks > num_31_blocks:
            return True

print('Part 2: ', sum([1 for m in messages if test_message(m)]))