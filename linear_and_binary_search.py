# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:19:14 2018

@author: `
"""

#linear and binary_search algorithms

def lin_search(lst,n):
    """(list,object)-->int
    returns index of n found, if not found returns -1 """
    
    for idx in range(len(lst)):
        if lst[idx]==n:
            return idx
    return -1
        
        
def binary_search(lst,n): 
    """(list,object)-->int
    returns index of n found, if not found returns -1 """
   
    i = 0 
    j = len(lst)-1
    while i<=j:
        m = (i+j)//2
        
        if lst[m] == n:
            return m
        elif lst[m] < n:
            i = m + 1
        else:
            j = m - 1
            
    return -1       



if __name__=='__main__':
    print(lin_search([1,2,3,7,8,10,20,50,1090,1123],50)) 
    print(binary_search([1,2,3,7,8,10,20,50,1090,1123],50))




