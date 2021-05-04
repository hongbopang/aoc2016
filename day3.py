# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:40:38 2021

@author: hongb
"""


f = open("day3input.txt")
ans1 = 0
ans2 = 0
counter = 0
total = 0
holder = [[0,0,0],[0,0,0],[0,0,0]]

for line in f:
    total += 3
    inputs = line.strip().split()     
    nums = list(map(int,inputs))
    
    for i in range(3):
        holder[i][counter] = nums[i]

    counter += 1
    if counter == 3:        
        for j in range(3):
            temp = holder[j]
            temp.sort()
            if temp[0] + temp[1] > temp[2]:
                ans2 += 1
        counter = 0
        holder = [[0,0,0],[0,0,0],[0,0,0]]

    nums.sort()
    if nums[0] + nums[1] > nums[2]:
        ans1 +=1
print(total)
print(ans1)
print(ans2)