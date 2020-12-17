import numpy as np

with open('data/inputd17.txt') as f:
    inputs = [x[0:-1] for x in f]

def process_cube(coords, active_log):
    number_active = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if (i, j, k) != (0, 0, 0):
                    if active_log.get(tuple(np.array(coords) + np.array([i, j, k]))):
                        number_active += 1
    
    if active_log.get(coords):
        if number_active in [2, 3]:
            return True
        else:
            return False
    else:
        if number_active == 3:
            return True
        else:
            return False
        
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
                buffer_active[(x, y, z)] = process_cube((x, y, z), active)
    active = buffer_active.copy()
    
    cycle += 1
    xmin -= 1
    xmax += 1
    ymin -= 1
    ymax += 1
    zmin -= 1
    zmax += 1
 
    
count_active = 0
for key in active:
    if active[key]:
        count_active += 1

print('Part 1: ', count_active)

# Part 2

def process_cube4d(coords, active_log):
    number_active = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if (i, j, k, l) != (0, 0, 0, 0):
                        if active_log.get(tuple(np.array(coords) + np.array([i, j, k, l]))):
                            number_active += 1
    
    if active_log.get(coords):
        if number_active in [2, 3]:
            return True
        else:
            return False
    else:
        if number_active == 3:
            return True
        else:
            return False
        
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
                    buffer_active[(x, y, z, w)] = process_cube4d((x, y, z, w), active)
    active = buffer_active.copy()
    
    cycle += 1
    xmin -= 1
    xmax += 1
    ymin -= 1
    ymax += 1
    zmin -= 1
    zmax += 1
    wmin -= 1
    wmax += 1
 
    
count_active = 0
for key in active:
    if active[key]:
        count_active += 1

print('Part 2: ', count_active)