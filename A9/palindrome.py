#A programme that uses a recursive function to calculate whether or not a string is a palindrome (reads the same if reversed). 
#Rector Ratsaka
#26 April 2022

def palindrome(string):
 if len(string)<=1:
  return True
 return string[0]==string[-1] and palindrome(string[1:-1])        

string=input("Enter a string:\n")
if palindrome(string):
 print("Palindrome!")
else :
 print("Not a palindrome!")  