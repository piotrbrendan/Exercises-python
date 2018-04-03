# -*- coding: utf-8 -*-

'''
From: Codewars

You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1

'''
## my solution

def next_bigger(n):

    l_total = [int(item) for item in str(n)]
    
    found = False
    for i in range(len(l_total)-1,0,-1):
        if l_total[i]>l_total[i-1] and found == False:
            lower = l_total[i-1]
            idx = i-1
            found = True
      
    if found == False:
        return -1
    
    l_left = l_total[:idx]        
    l_right = l_total[idx+1:]
    
    next_lower = min(list(filter(lambda x: x>lower, l_right)))
    
    del l_right[l_right.index(next_lower)]
    
    result = l_left + [next_lower] + sorted(l_right+[lower])
    result = "".join(map(str,result))
    
    return int(result)


if __name__ =='__main__':
    print(next_bigger(144))
    print(next_bigger(441))
    print(next_bigger(10756432))