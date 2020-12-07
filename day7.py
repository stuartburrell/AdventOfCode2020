with open('data/inputd7.txt') as f:
    inputs = [x for x in f]

# Clean input
    
for i in range(len(inputs)):
    inputs[i] = inputs[i].split(' contain ')
    for j in range(len(inputs[i])):
        inputs[i][j] = inputs[i][j].replace(' bags', '').replace(
                                            ' bag', '').replace(
                                            ' ','')
    inputs[i][1] = inputs[i][1][:-2].split(',')
 
# Arrange data as a dictionary

rules = dict()
for rule in inputs:
    if rule[1] == ['noother']:
        rules[rule[0]] = []
    else:
        rules[rule[0]] = [(int(x[0]), x[1:]) for x in rule[1]]

# Recursive function to compute possible bag containments
        
def possible_bags(colour, log = set(), seen = []):
    seen = seen + [colour]
    log  = log.union(set([x[1] for x in rules[colour]]))
    for col in log:
        if col not in seen:
            return log.union(possible_bags(col, log, seen))
    return log

# Total number of outer bags that eventually contain a shiny gold bag
    
total_count = 0
for key in rules.keys():
    if 'shinygold' in possible_bags(key):
        total_count += 1
        
print('Part 1: ', total_count)

# Recursive function to count number of bags contained in given bag

def bag_counter(col):
    if rules[col] == []:
        return 0
    else:
        return sum([x[0] + x[0] * bag_counter(x[1]) for x in rules[col]])

print('Part 2: ', bag_counter('shinygold'))