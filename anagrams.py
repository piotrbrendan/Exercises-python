#!/opt/anaconda3/bin/python

# return True jesli s i t sa anagramami,
# return False w przeciwnym wypadku
def anagrams(s,t):
   """(str,str)->bool
   return True jesli s i t sa anagramami,
   return False w przeciwnym wypadku
   zalozylem, ze wielkosc liter nie ma znaczenia
   """
   char_s_list=[]
   char_t_list=[]
    
   if len(s)!=len(t):
       return False
   
   for char in s:
       char_s_list.append(char.upper())
   char_s_list.sort()
    
   for char in t:
       char_t_list.append(char.upper())       
   char_t_list.sort()
   
   return char_s_list==char_t_list

          
if __name__ == "__main__":
  s1 = input()
  s2 = input()
  res = anagrams(s1,s2)
  print("1" if res else "0")
  
  