with open('data/inputd18.txt') as f:
    inputs = [x[0:-1].replace(' ', '') for x in f]

def convert_string_to_list(string):
    output = [string[0]]
    i  = 1
    while i < len(string):
        if string[i].isnumeric():
            if output[-1].isnumeric():
                output[-1] += string[i]
            else:
                output.append(string[i])
        else:
            output.append(string[i])
        i += 1
    return output

def basic_sum(string, advanced):
    if advanced:
        parsed = convert_string_to_list(string)
        i = 0
        while i < len(parsed):
            if parsed[i] == '+':
                parsed = parsed[0:i - 1] + [str(int(parsed[i - 1]) + int(parsed[i + 1]))] + parsed[i + 2:]
                i -= 2
            i += 1
            eq_list = convert_string_to_list(parsed)
    else:
        eq_list = convert_string_to_list(string) 
    output = int(eq_list[0])
    for i in range(1, len(eq_list)):
        if eq_list[i].isnumeric():
            if eq_list[i - 1] == '+':
                output += int(eq_list[i])
            else:
                output *= int(eq_list[i])
    return output

def process_string(string, advanced):
    parsed = string
    while '(' in parsed or ')' in parsed:
        i = 0
        while i < len(parsed):
            if parsed[i] != '(':
                i += 1
            else:
                start = i
                j = i + 1
                while j < len(parsed):
                    if parsed[j] == ')':
                        parsed = parsed[:start] + str(basic_sum(parsed[start + 1:j], advanced)) + parsed[j + 1:]
                        i = 0
                        j = len(parsed)
                    elif parsed[j] == '(':
                        i = j  
                        j = len(parsed)
                    else:
                        j += 1
    return basic_sum(parsed, advanced)

# Part 1

print('Part 1: ', sum([process_string(x, advanced = False) for x in inputs]))

# Part 2

print('Part 2: ', sum([process_string(x, advanced = True) for x in inputs]))   