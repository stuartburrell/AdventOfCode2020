import numpy as np

with open('data/inputd12.txt') as f:
    inputs = [(x[0], int(x[1:])) for x in f]
    
# Part 1

def move(instructions):
    facing = 0
    directions = {0 : 'E', 90:'N', 180:'W', 270:'S'}
    move = {'N':0, 'E':0, 'S':0, 'W':0}
    for x in instructions:
        if x[0] == 'F':
            move[directions[facing]] += x[1]
        elif x[0] == 'L':
            facing = (facing + x[1]) % 360
        elif x[0] == 'R':
            facing = (facing - x[1]) % 360
        else:
            move[x[0]] += x[1]
    return [move['E'] - move['W'], move['N'] - move['S'], directions[facing]]

print('Part 1: ', abs(sum(move(inputs)[0:2])))

# Part 2

def rotate_vector(vec, angle):
    if angle == 90:
        return np.matmul(np.array([[0, -1],[1, 0]]), vec)
    elif angle == 180:
        return -vec
    elif angle == 270:
        return np.matmul(np.array([[0, 1],[-1, 0]]), vec)

def move_waypoint(instructions):
    ship = np.array([0, 0])
    waypoint = np.array([10, 1])
    for x in instructions:
        if x[0] == 'F':
            ship = ship + x[1] * waypoint
        if x[0] == 'L':
            waypoint = rotate_vector(waypoint, x[1])
        if x[0] == 'R':
            waypoint = rotate_vector(waypoint, (360 - x[1]))
        if x[0] == 'N':
            waypoint[1] = waypoint[1] + x[1]
        if x[0] == 'E':
            waypoint[0] = waypoint[0] + x[1]
        if x[0] == 'S':
            waypoint[1] = waypoint[1] - x[1]
        if x[0] == 'W':
            waypoint[0] = waypoint[0] - x[1]
    return abs(ship[0]) + abs(ship[1])

print('Part 2: ', move_waypoint(inputs))