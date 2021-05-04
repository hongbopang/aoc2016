# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:49:35 2021

@author: hongb
"""


x = 0
y = 0

direction = 0


addrs = dict()
flag = True
file = open("day1input.txt")
for line in file:
    inputs = line.split(",")

for entry in inputs:
    entry = entry.strip()
    movement = int(entry[1:])    
    
    
    if entry[0] == "L":
       direction = (direction - 1) % 4
    elif entry[0] == "R":
        direction = (direction + 1) % 4

        
    if direction == 0:
        for _ in range(movement):            
            y += 1
            addr = str(x) + ',' + str(y)
            if addr in addrs and flag:
                print(abs(x)+abs(y))
                flag = False
            else:
                addrs[addr] = 1
        
    elif direction == 1:
        for _ in range(movement):            
            x += 1
            addr = str(x) + ',' + str(y)
            if addr in addrs and flag:
                print(abs(x)+abs(y))
                flag = False
            else:
                addrs[addr] = 1
        
    elif direction == 2:
        for _ in range(movement):            
            y -= 1
            addr = str(x) + ',' + str(y)
            if addr in addrs and flag:
                print(abs(x)+abs(y))
                flag = False
            else:
                addrs[addr] = 1
        
    else:
        for _ in range(movement):            
            x -= 1
            addr = str(x) + ',' + str(y)
            if addr in addrs and flag:
                print(abs(x)+abs(y))
                flag = False
            else:
                addrs[addr] = 1
    

    

print(abs(x)+abs(y))
