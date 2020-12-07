from itertools import product

with open('data/inputd1.txt') as f:
    nums = [int(x) for x in f]

# Part 1

for i, j in product(nums, nums):
    if i + j == 2020:
        print('Part 1: ', i * j)
        break
            
# Part 2 
                
for i, j, k in product(nums, nums, nums):
    if i + j + k == 2020:
        print('Part 2: ', i * j * k)
        break