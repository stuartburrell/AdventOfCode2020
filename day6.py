with open('data/inputd6.txt') as f:
    inputs = [x for x in f]

groups = ['']
index = 0
for x in inputs:
    if x == '\n':
        groups.append('')
        index += 1
    else:
        groups[index] += x
        
# Part 1
        
groups_flat = [x[:-1].replace('\n', '') for x in groups]
print('Part 1: ', sum([len(x) for x in [set(x) for x in groups_flat]]))

# Part 2

groups_split = [x.split('\n')[:-1] for x in groups]
print('Part 2: ', sum([len(set.intersection(*[set(i) for i in g])) 
                       for g in groups_split]))