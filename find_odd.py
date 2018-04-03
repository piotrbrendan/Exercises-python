# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:44:33 2018

@author: `
"""

'''
From: Codewars
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''


def find_it(seq):
    d={}
    for i in seq:
        d[i] = d.get(i,0)+1
    
    for item, value in d.items():
        if value%2 !=0:
            return item
        
        
if __name__=='__main__':
    print(find_it([5,5,4,4,4,4,21]))
    print(find_it([2,2,4,4,3,3,3,21,21]))