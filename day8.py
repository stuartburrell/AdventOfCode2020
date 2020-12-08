import copy

with open('data/inputd8.txt') as f:
    inputs = [(x[:-1].split(' ')[0], int(x[:-1].split(' ')[1])) for x in f]
    
# Part 1
    
def run(prog):
    accumalator = 0
    position = 0
    seen = []
    stop = False
    success = False
    n = len(prog)
    while not stop:
        if position not in seen:
            seen.append(position)
        else:
            stop = True     
        if prog[position][0] == 'nop':
            position += 1
        elif prog[position][0] == 'acc':
            accumalator += prog[position][1]
            position +=1
        elif prog[position][0] == 'jmp':
            position += prog[position][1]
        if position >= n:
            stop = True
            success = True
    return [position, accumalator, success] 

print('Part 1: ', run(inputs)[1])

# Part 2

for i in range(len(inputs)):
    test_inputs = copy.copy(inputs)
    if inputs[i][0] == 'jmp':
        test_inputs[i] = ('nop', test_inputs[i][1])
        output = run(test_inputs)
        if output[2] == True:
            print('Part 2: ', output[1])