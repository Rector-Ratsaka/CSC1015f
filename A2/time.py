#Checking validity of time.
#RTSREC001
#28 February 2022

h = int(input("Enter the hours:\n"))
m = int(input("Enter the minutes:\n"))
s = int(input("Enter the seconds:\n"))
if 0 <= h <= 23:
   if 0 <= m <= 59:
      if 0 <= s <= 59:
         print("Your time is valid.")
      else: 
         print("Your time is invalid.")
   else: 
      print("Your time is invalid.")
else: 
   print("Your time is invalid.")      