# Part 1

with open('data/inputd13.txt') as f:
    inputs = [x[0:-1] for x in f]
    
target = int(inputs[0])
ids = [int(y) for y in inputs[1].replace('x', '').split(',') if len(y) > 0]

wait_times = [i - (target % i) for i in ids]
ind_best_bus = min(range(len(wait_times)), key=wait_times.__getitem__)

print('Part 1: ', ids[ind_best_bus]*wait_times[ind_best_bus] )

# Part 2

offsets = {x : inputs[1].split(',').index(str(x)) for x in ids}

'''
 Apply Chinese Remainder Theorem: we seek t such that
 
t mod 23 = 0
t mod 41 = 41 - 13
t mod 733 = 733 - 23
.
.
.
t mod bus_ID = bus_ID - offset[bus_ID]

Using a standard CRT solver: t = 775230782877242.
'''

print('Part 2: ', 775230782877242)