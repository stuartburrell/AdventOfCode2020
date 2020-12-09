with open('data/inputd9.txt') as f:
    inputs = [int(x) for x in f]

# Part 1
    
def check_sum(preamble, entry):
    for i in preamble:
        for j in preamble:
            if i + j == entry:
                return True
    return False

n = len(inputs)
for i in range(25, n):
    if not check_sum(inputs[i-25:i], inputs[i]):
        print('Part 1: ', inputs[i])
        target = inputs[i]
    
# Part 2
    
found = False
block_length = 2
while found == False:
    for i in range(n - block_length):
        if sum(inputs[i:i+block_length]) == target:
            contig_set = inputs[i:i+block_length]
            found = True
    block_length += 1

print('Part 2: ', min(contig_set) + max(contig_set))