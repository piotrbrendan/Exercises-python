# -*- coding: utf-8 -*-

def longestPalSubstr1(s):
    '''Returns -1 for single letter palindromes. Lower and upper cases matter
    '''
    
    lmax=''
    for i in range(len(s)-1):
        l=s[i:]
        for i in range(len(l)):
            l1 = l[:i+2]
            lp = l1[::-1]
            if l1 == lp and len(l1)>len(lmax):
                lmax = l1
    if len(lmax) <= 1:
        return -1
    return lmax



### different approach below:         
def longestPalSubstr2(string):
    maxLength = 1
    start = 0
    length = len(string)
 
    low = 0
    high = 0
 
    # One by one consider every character as center point of odd
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
    # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
                
            low -= 1
            high += 1
        # Find the longest odd length palindrome with center 
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
                
            low -= 1
            high += 1
    print ("Longest palindrome substring is:")
    print (string[start:(start + maxLength)])
 
    return maxLength


if __name__ =='__main__':
    print(longestPalSubstr1('wanna'))
    print(longestPalSubstr2('walannala'))
    
    

