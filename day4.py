# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:51:34 2021

@author: hongb
"""
line = "aaaaa-bbb-z-y-x-123[abxyz]"

def check(line):
    code,checksum = line.split("[")
    checksum = checksum[:-1]

    codes = code.split("-")
    
    