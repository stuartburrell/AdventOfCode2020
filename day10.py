from itertools import chain, combinations
from math import prod

with open('data/inputd10.txt') as f:
    inputs = [int(x) for x in f]
    
inputs.insert(0, 0)
inputs.insert(-1, max(inputs) + 3)
inputs.sort()
n = len(inputs)

# Part 1

diffs = [0, 0, 0]
for i in range(1, n):
    diffs[inputs[i] - inputs[i - 1] - 1] += 1
    
print('Part 1: ', diffs[0] * diffs[2])

# Part 2

def check_valid(nums):
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) not in [1, 2, 3]:
            return False
    return True

def powerset(iterable):
    s = list(iterable)
    ch = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return [list(x) for x in ch]

def valid_substrings(nums):
    total = 0
    if nums[0] == 0 and nums[1] == 1:
         ps = powerset(nums[1:-2])
         for p in ps:
             if check_valid(nums[:1] + p + nums[-2:]):
                 total += 1
         return total  
    ps = powerset(nums[2:-2])
    for p in ps:
        if check_valid(nums[:2] + p + nums[-2:]):
            total += 1
    return total

'''

Sort input into regular groups of the form:
[n, n + 3, n + 4, n + 5, ... n + k, (n + k) + 3]

'''

groups = [[0]]
ones = inputs[1] - inputs[0] == 1
for i in range(1, n):
    groups[-1].append(inputs[i])
    if ones:
        if inputs[i] - inputs[i - 1] != 1:
            ones = False
            groups.append([inputs[i-1], inputs[i]])
    else: 
        if inputs[i] - inputs[i - 1] != 3:
            ones = True      

perms = [valid_substrings(x) for x in groups]
print('Part 2: ', prod(perms))