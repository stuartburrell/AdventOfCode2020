with open('data/inputd10.txt') as f:
    inputs = [int(x) for x in f]

inputs.sort()
n = len(inputs)

# Part 1

diffs = [1, 0, 1]
for i in range(1, n):
    diffs[inputs[i] - inputs[i - 1] - 1] += 1
    
print('Part 1: ', diffs[0] * diffs[2])

# Part 2

num_paths = {x:0 for x in range(-2, max(inputs))}
num_paths[0] = 1
for value in inputs:
    num_paths[value] = sum([num_paths[value - i] for i in range(1, 4)])

print('Part 2: ', num_paths[max(inputs)])