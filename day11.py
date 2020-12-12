import numpy as np

with open('data/inputd11.txt') as f:
    inputs = [x[:-1] for x in f]

nrows = len(inputs)
ncols = len(inputs[0])

seating_array = np.zeros((nrows, ncols), dtype = int)
for i in range(nrows):
    for j in range(ncols):
        if inputs[i][j] == 'L':
            seating_array[i][j] = -1
            
# Key: empty = -1, floor = 0, occupied = 1

# Part 1

def iterate_seat(row, col, plan, nr = nrows, nc = ncols):
    occupied = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if row + i < nr and row + i >= 0:
                if col + j < nc and col + j >= 0:
                    if not (i == 0 and j == 0):
                        if plan[row + i, col + j] == 1:
                            occupied += 1
    if occupied >= 4:
        return -1
    elif occupied == 0:
        return 1
    else:
        return plan[row, col]
    
def iterate_plan(seating_plan):
    new_plan = seating_plan.copy()
    for i in range(nrows):
        for j in range(ncols):
            if new_plan[i, j] != 0:
                new_plan[i, j] = iterate_seat(i, j, seating_plan)
    return new_plan

change = True
current_plan = seating_array

while change:
    new_plan = iterate_plan(current_plan)
    if np.array_equal(new_plan, current_plan):
        change = False
    else:
        current_plan = new_plan.copy()
        
print('Part 1: ', np.count_nonzero(current_plan == 1))

# Part 2

def horizontal_view(row, col, plan, nr = nrows, nc = ncols):
    visible = 0
    i = 1
    while col + i < nc:
        if plan[row, col + i] == 1:
            visible += 1
            i = nc
        elif plan[row, col + i] == -1:
            i = nc
        i += 1
        
    i = 1
    while col - i >= 0:
        if plan[row, col - i] == 1:
            visible += 1
            i = 2*nc
        elif plan[row, col - i] == -1:
            i = 2*nc
        i += 1
    return visible

def vertical_view(row, col, plan, nr = nrows, nc = ncols):
    visible = 0
    i = 1
    while row + i < nr:
        if plan[row + i, col] == 1:
            visible += 1
            i = nr
        elif plan[row + i, col] == -1:
            i = nr
        i += 1
    i = 1
    while row - i >= 0:
        if plan[row - i, col] == 1:
            visible += 1
            i = 2*nr
        elif plan[row - i, col] == -1:
            i = 2*nr
        i += 1
    return visible
            
def diagonal_view(row, col, plan, nr = nrows, nc = ncols):
    visible = 0
    i = 1
    while row + i < nr and col + i < nc:
        if plan[row + i, col + i] == 1:
            visible += 1
            i = 2*nc
        elif plan[row + i, col + i] == -1:
            i = 2*nc
        i += 1
    i = 1
    while row - i >= 0 and col - i >= 0:
        if plan[row - i, col - i] == 1:
            visible += 1
            i = nc + nr
        elif plan[row - i, col - i] == -1:
            i = nc + nr
        i += 1
    i = 1
    while row + i < nr and col - i >= 0:
        if plan[row + i, col - i] == 1:
            visible += 1
            i = 2*nr
        elif plan[row + i, col - i] == -1:
            i = 2*nr
        i += 1
    i = 1
    while row - i >= 0 and col + i < nc:
        if plan[row - i, col + i] == 1:
            visible += 1
            i = 2*nr
        elif plan[row - i, col + i] == -1:
            i = 2*nr
        i += 1
    return visible
        
def iterate_seat_vis(row, col, plan, nr = nrows, nc = ncols):
    visible = 0
    visible += horizontal_view(row, col, plan, nr = nrows, nc = ncols)
    visible += vertical_view(row, col, plan, nr = nrows, nc = ncols)
    visible += diagonal_view(row, col, plan, nr = nrows, nc = ncols)
    if visible >= 5:
        return -1
    elif visible == 0:
        return 1
    else:
        return plan[row, col]

def iterate_plan_vis(seating_plan):
    new_plan = seating_plan.copy()
    for i in range(nrows):
        for j in range(ncols):
            if new_plan[i, j] != 0:
                new_plan[i, j] = iterate_seat_vis(i, j, seating_plan)
    return new_plan

change = True
current_plan = seating_array

while change:
    new_plan = iterate_plan_vis(current_plan)
    if np.array_equal(new_plan, current_plan):
        change = False
    else:
        current_plan = new_plan.copy()
        
print('Part 2: ', np.count_nonzero(current_plan == 1))