#A programme that may be used to assist with debugging Python programs.
#Rector Ratsaka
#01 May 2022

print("***** Program Trace Utility *****")
program = input("Enter the name of the program file: ")
file = open(program,"r+")
write = "\"\"\"DEBUG\"\"\"\n"
update = ""
read = file.readlines()
if "\"\"\"DEBUG\"\"\"" in read[0]:
 for line in read:
  if "\"\"\"DEBUG\"\"\"" not in line:
   update = update + line
 
 file.seek(0)
 file.truncate()
 file.write(update) 
 print("Removing...Done")
else:
 for line in read:
  if "def" in line:
   write = write + line
   index = line.index("(")
   function = line[0:index].replace("def","")
   write = write +"    \"\"\"DEBUG\"\"\";print('"+function.strip()+"')"+"\n"
  else:
   write = write + line
 
 file.seek(0)
 file.truncate()
 file.write(write)
 print("Inserting...Done")
file.close()