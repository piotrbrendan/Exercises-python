# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:03:46 2018

@author: `
"""

def if_equals_str_len(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''       
    return sum([x == len(L2[i]) for i,x in enumerate(L1)]) == len(L1) 


if __name__ =='__main__':
    
    print(if_equals_str_len([1,2,3,4],['a','xo','www','abba']))
    print(if_equals_str_len([1,2,3,4],['a','xoxo','www','abba']))
