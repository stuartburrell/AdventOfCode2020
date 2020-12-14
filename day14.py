from itertools import product

with open('data/inputd14.txt') as f:
    inputs = [x[0:-1] for x in f]
    
for i in range(len(inputs)):
    inputs[i] = inputs[i].split(' = ')
    if inputs[i][0] != 'mask':
        inputs[i] = [int(inputs[i][0][4:-1]), int(inputs[i][1])]

# Part 1

def apply_mask(number, mask):
    reverse_mask = mask[::-1]
    bin_num = list(bin(number)[2:])[::-1] 
    bin_num = bin_num + ['0' for x in mask[len(bin_num):]]
    for i in range(len(bin_num)):
        if reverse_mask[i] != 'X':
            bin_num[i] = reverse_mask[i]
    return int(''.join(bin_num)[::-1], 2)

mem = {}

for x in inputs:
    if x[0] == 'mask':
        mask = x[1]
    else:
        mem[x[0]] = apply_mask(x[1], mask)
    

print('Part 1: ', sum(mem.values()))

# Part 2

def mask_address(address, mask):
    reverse_mask = mask[::-1]
    add_num = list(bin(address)[2:])[::-1] 
    add_num = add_num + ['0' for x in mask[len(add_num):]]
    for i in range(len(add_num)):
        if reverse_mask[i] != '0':
            add_num[i] = reverse_mask[i]
    return ''.join(add_num)[::-1]

mem = {}
for x in inputs:
    if x[0] == 'mask':
        mask = x[1]
    else:
        add = mask_address(x[0], mask)
        x_pos = [pos for pos, char in enumerate(add) if char == 'X']
        add = list(add)
        for seq in product([0,1], repeat = len(x_pos)):
            for p in range(len(x_pos)):
                add[x_pos[p]] = str(seq[p])
            mem[int(''.join(add), 2)] = x[1]
            
print('Part 2: ', sum(mem.values()))