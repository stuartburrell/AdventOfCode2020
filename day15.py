inputs = [19, 0, 5, 1, 10, 13]

def nth_number(n, starters):
    
    times_seen = {starters[i]: 1 for i in range(len(starters))}
    seen = {starters[i]: [i + 1] for i in range(len(starters))}
    last_number = starters[-1]
    
    turn = len(starters) + 1
    while turn < n + 1:
        if times_seen[last_number] == 1:
            last_number = 0
        else:
            last_number = seen[last_number][1] - seen[last_number][0] 
        if seen.get(last_number) != None:
            seen[last_number] = [seen[last_number][-1], turn]
            times_seen[last_number] += 1
        else:
            seen[last_number] = [turn]
            times_seen[last_number] = 1
        turn += 1
    return last_number

# Part 1

print('Part 1: ', nth_number(2020, inputs))

# Part 2

print('Part 2: ', nth_number(30000000, inputs))