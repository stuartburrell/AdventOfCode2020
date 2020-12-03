#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Part 1

with open('inputp2.txt') as f:
    inputs = [x for x in f]
    
def process(raw):
    output = raw.split(' ')
    lower = int(output[0].split('-')[0])
    upper = int(output[0].split('-')[1])
    letter = output[1][0]
    string = output[2][0:-1]
    return([string, lower, upper, letter])
    
def test1(string, lower, upper, letter):
    count = 0
    for s in string:
        if s == letter:
            count += 1
    if lower <= count <= upper:
        return True
    return False

total1 = 0
for raw in inputs:
    proc = process(raw)
    if test1(proc[0], proc[1], proc[2], proc[3]):
        total1 +=1 
        
print('Part 1: ', total1)

# Part 2
 
def test2(string, pos1, pos2, letter):
    count = 0
    if string[pos1 - 1] == letter:
        count +=1
    if string[pos2 - 1] == letter:
        count += 1
    if count == 1:
        return True
    return False

total2 = 0
for raw in inputs:
    proc = process(raw)
    if test2(proc[0], proc[1], proc[2], proc[3]):
        total2 +=1 
        
print('Part 2: ', total2)