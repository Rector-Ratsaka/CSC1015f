# A programme that uses a recursive function to count the number of pairs of consecutive characters in a string.
#Rector Ratsaka
#26 April 2022

def pairs(string):
 if len(string) <= 1:
  return 0
 if string[0] == string[1]:
  return 1 + pairs(string[2:])
 else:
  return pairs(string[1:])    
    
string = input('Enter a message:\n')
print('Number of pairs:',str(pairs(string)))