# Part 1

with open('data/inputd13.txt') as f:
    inputs = [x[0:-1] for x in f]
    
target = int(inputs[0])
ids = [int(y) for y in inputs[1].replace('x', '').split(',') if len(y) > 0]

wait_times = [i - (target % i) for i in ids]
ind_best_bus = min(range(len(wait_times)), key=wait_times.__getitem__)

print('Part 1: ', ids[ind_best_bus]*wait_times[ind_best_bus] )

# Part 2

'''
Apply Chinese Remainder Theorem: we seek t such that
 
t mod 23 = 0
t mod 41 = 41 - 13
t mod 733 = 733 - 23
.
.
.
t mod bus_ID = bus_ID - offset[bus_ID]

CRT code: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
'''
     
from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

offsets = {x : inputs[1].split(',').index(str(x)) for x in ids}
remainders = [x - offsets[x] for x in ids]

print('Part 2: ', chinese_remainder(ids, remainders))