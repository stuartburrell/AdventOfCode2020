# Part 1

with open('inputp5.txt') as f:
    inputs = [[x[:-4], x[-4:-1]] for x in f]
    
def row(string):
    string = string.replace('F','0').replace('B', '1')
    return int(string, 2)

def col(string):
    string = string.replace('L','0').replace('R', '1')
    return int(string, 2)

def seat_id(row, col):
    return 8*row + col

seat_ids = [seat_id(row(x[0]), col(x[1])) for x in inputs]

print('Part 1: ', max(seat_ids))

# Part 2

seat_ids.sort()
for i in range(len(seat_ids)-1):
    if seat_ids[i + 1] != seat_ids[i] + 1:
        print('Part 2: ', seat_ids[i] + 1)