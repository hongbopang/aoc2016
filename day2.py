# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:42:13 2021

@author: hongb
"""

file = open("day2input.txt")

key = [[1,2,3],[4,5,6],[7,8,9]]

x = 1
y = 1

ans = 0


for line in file:
    commands = [char for char in line.strip()]
    for cmd in commands:
        if cmd == 'R' and x != 2:
            x += 1
        elif cmd == 'L' and x != 0:
            x -= 1
        elif cmd == "U" and y != 0:
            y -= 1
        elif cmd =="D" and y != 2:
            y += 1

    ans *= 10
    ans += key[y][x]
    
print(ans)

file = open("day2input.txt")
key = [[0,0,"1",0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A","B","C",0],[0,0,"D",0,0]]

x = 0
y = 2

xtemp = 0
ytemp = 2

ans = ""

for line in file:
    commands = [char for char in line.strip()]
    for cmd in commands:
        if cmd == 'R' and x != 4:
            xtemp = x+1
        elif cmd == 'L' and x != 0:
            xtemp = x-1
        elif cmd == "U" and y != 0:
            ytemp = y-1
        elif cmd =="D" and y != 4:
            ytemp = y+1
        if key[ytemp][xtemp] != 0:
            x = xtemp
            y = ytemp
        xtemp = x
        ytemp=y
    
    ans += str(key[y][x])
    
print(ans)