import numpy as np
from itertools import product

with open('data/inputd17.txt') as f:
    inputs = [x[0:-1] for x in f]

def process_cube(coords, active_log, dimension):
    number_active = 0
    for increment in product([-1, 0, 1], repeat = dimension):
        if increment != tuple([0 for i in range(dimension)]):
            if active_log.get(tuple(np.array(coords) + np.array(increment))):
                        number_active += 1  
    if active_log.get(coords):
        if number_active in [2, 3]:
            return True
    else:
        if number_active == 3:
            return True
    return False

# Part 1
        
active = {}
for i, row in enumerate(inputs):
    for j, char in enumerate(row):
        active[(i, j, 0)] = (char == '#')

xmin, xmax = -1, len(inputs[0]) 
ymin, ymax = -1, len(inputs) 
zmin, zmax = -1, 1

cycle = 1
while cycle < 7:
    buffer_active = active.copy()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                buffer_active[(x, y, z)] = process_cube((x, y, z), active, 3)
    active = buffer_active.copy()
    
    xmin, xmax = xmin - 1, xmax + 1
    ymin, ymax = ymin - 1, ymax + 1
    zmin, zmax = zmin - 1, zmax + 1
    cycle += 1

print('Part 1: ', sum([1 for key in active if active[key] == True]))

# Part 2
 
active = {}
for i, row in enumerate(inputs):
    for j, char in enumerate(row):
        active[(i, j, 0, 0)] = (char == '#')

xmin, xmax = -1, len(inputs[0]) 
ymin, ymax = -1, len(inputs) 
zmin, zmax = -1, 1
wmin, wmax = -1, 1

cycle = 1
while cycle < 7:
    buffer_active = active.copy()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                for w in range(wmin, wmax + 1):
                    buffer_active[(x, y, z, w)] = process_cube((x, y, z, w), 
                                                               active, 4)
    active = buffer_active.copy()

    xmin, xmax = xmin - 1, xmax + 1
    ymin, ymax = ymin - 1, ymax + 1
    zmin, zmax = zmin - 1, zmax + 1
    wmin, wmax = wmin - 1, wmax + 1
    cycle += 1

print('Part 2: ', sum([1 for key in active if active[key] == True]))