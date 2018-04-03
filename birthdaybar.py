#!/opt/anaconda3/bin/python

import sys

def solve(n, s, d, m):
    '''(int,list of int, int, int)->int
    '''
    assert n>=1,        'n is lower than 1'
    assert len(s)==n,   'len of s list does not match n'
    assert 1<=d<=31,    'd is not between <1,31>'
    assert 1<=m<=12,    'm is not between <1,12>'
    
    count=0
    total=0
    
    if d<m:
        count=0
    else:  
        for i in range(len(s)-(m-1)):
            total=sum(s[i:(i+m)]) 
            if total==d:
                count=count+1
                   
    return count
  


if __name__ == "__main__":
  n = int(input().strip())
  s = list(map(int, input().strip().split(' ')))
  d, m = input().strip().split(' ')
  d, m = [int(d), int(m)]
  result = solve(n, s, d, m)
  print(result)
  
###############################
###############################  
  
