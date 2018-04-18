# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:32:56 2018

The word i18n is a common abbreviation of internationalization in the developer 
community, used instead of typing the whole word and trying to spell it correctly. 
Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) 
within that string of length 4 or greater into an abbreviation, following these rules:

A "word" is a sequence of alphabetical characters. By this definition, 
any other character like a space or hyphen (eg. "elephant-ride") will 
split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, 
then the number of removed characters, then the last letter 
(eg. "elephant ride" => "e6t r2e").

Example

abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"

"""
import re

def abbreviate(s):
    '''first solution without regex'''

    output=[]
    i=0
    while i<len(s):
        word =''
        while i <= len(s) and s[i].isalpha():
           word +=s[i] 
           i+=1 
        transf_word = word[0]+str(len(word[1:-1]))+word[-1] if len(word)>3 else word
        output.append(transf_word)
           
        if i <= len(s) and not s[i].isalpha():
            output.append(s[i])
            i +=1
            
    return ''.join(output)


############ solution with regex ###########################
    
def change(m):
    word = m.group(0)
    transf_word = word[0] + str(len(word[1:-1])) + word[-1] 
    return transf_word

def abbreviate2(s):
    '''second solution with regex'''    
    return re.sub('[a-zA-Z]{4,}',change,s)

if __name__=='__main__':
    print(abbreviate('Why don\'t you just print it?! High 5.'))
    print(abbreviate2('No idea why 2 people can\'t deal with each other'))
