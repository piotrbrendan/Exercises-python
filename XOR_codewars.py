# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:30:04 2018

@author: `

Description :
Given a string consisting entirely of binary digits (0 , 1) seperated using spaces.
Find the XOR of all digits and return the answer.

Examples :
1 0 0 1 0 --> 0
1 0 1 1 1 0 0 1 0 0 0 0 --> 1

HOW:
1 0 0 1 0

(1 XOR 0) (0 XOR 1) 0
1 1 0
(1 XOR 1) 0
0 0
0 XOR 0
0 ---> Answer

"""

def XOR(s):
    return sum(map(int,s.split()))%2

if __name__ ='__main__':
    print(XOR('1 0 0 1 0'))
    print(XOR('1 0 1 1 1 0 0 1 0 0 0 0'))
