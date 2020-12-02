#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:17:38 2020

@author: stuartburrell
"""

with open('inputp1.txt') as f:
    nums = [int(x) for x in f]
    
nums.sort()

nums = [x for x in nums if x <= 2020 - nums[0] - nums[1]]

for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                print(i*j*k)