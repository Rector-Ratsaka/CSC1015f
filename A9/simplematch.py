#A programme that contains a recursive function called ‘match(pattern, word)’, that can be used to determine if a given pattern matches a given word.
#Rector Ratsaka
#26 April 2022

def match(pattern, word):
 if pattern==word :
  return True
 if pattern=='' or word=='':
  return False
 if pattern[0]==word[0] or pattern[0]=='?':
  return match(pattern[1:], word[1:]) 
 


 
 
