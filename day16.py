with open('data/inputd16.txt') as f:
    inputs = [x for x in f]
    
fields = inputs[0:20]
for i in range(len(fields)):
    fields[i] = fields[i][0:-1].split(': ')
    fields[i][1] = fields[i][1].split(' or ')
    fields[i][1][0] = fields[i][1][0].split('-')
    fields[i][1][1] = fields[i][1][1].split('-')
    fields[i].append(fields[i][1][1])
    fields[i][1] = fields[i][1][0]
    fields[i][1] = [int(x) for x in fields[i][1]]
    fields[i][2] = [int(x) for x in fields[i][2]]
    
nrby_tickets = [ [int(y) for y in x.split(',')] for x in inputs[25:]]

# Part 1

def check_int(number, rules):
    for rule in rules:
        if number >= rule[1][0] and number <= rule[1][1]:
            return True
        elif number >= rule[2][0] and number <= rule[2][1]:
            return True
    return False

error_rate = 0
valid_tickets = []
for t in nrby_tickets:
    switch = 1
    for entry in t:
        if not check_int(entry, fields):
            error_rate += entry
            switch = 0
    if switch == 1:
        valid_tickets.append(t)
            
print('Part 1: ', error_rate)

# Part 2

field_names = [x[0] for x in fields]
field_positions = {i : [x for x in field_names] for i in range(len(fields))}

for t in valid_tickets:
    for i, entry in enumerate(t):
        for rule in fields:
            if not check_int(entry, [rule]):
                if rule[0] in field_positions[i]:
                    field_positions[i].remove(rule[0])

changed = True
while changed:
    changed = False
    for pos in field_positions.keys():
        if len(field_positions[pos]) == 1:
            for x in field_positions.keys():
                if x != pos:
                    if field_positions[pos][0] in field_positions[x]:
                        field_positions[x].remove(field_positions[pos][0])
                        changed = True


myticket = [int(x) for x in inputs[22].split(',')]
prod = 1
for key in field_positions.keys():
    if field_positions[key][0][0:9] == 'departure':
        prod = prod * myticket[key]
        
print('Part 2: ', prod)