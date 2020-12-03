# -*- coding: utf-8 -*-

with open('inputp3.txt') as f:
    inputs = [[x[0:-1]] for x in f]
        
def tree_counter(tree_map, right, down):
    current = [0, 0]
    total_trees = 0
    depth = len(inputs)
    while current[0] < depth:
        if inputs[current[0]][0][current[1]] == '#':
            total_trees += 1
        current[0] += down
        current[1] = (current[1] + right) % len(inputs[0][0])
    return(total_trees)
    
print('Part 1: ', tree_counter(inputs, 3, 1))
print('Part 2: ', 
      tree_counter(inputs, 1, 1)*
      tree_counter(inputs, 3, 1)*
      tree_counter(inputs, 5, 1)*
      tree_counter(inputs, 7, 1)*
      tree_counter(inputs, 1, 2))