#A programme that asks the user to enter a word length and a filename.
#Rector Ratsaka
#01 May 2022

print("***** Anagram Set Search *****")
length = int(input("Enter word length:\n"))
print("Searching...")
filename = input("Enter file name:\n")
print("Writing results...")
file = open("EnglishWords.txt","r")
array = file.readlines()
file.close()
sets = []
for element in array:
 element = element.replace("\n","")
 if length == len(element):
  sets.append(element)
  
def anagrams(word):
 file = open("EnglishWords.txt","r")
 arrayfile = file.readlines()
 dictWord = {}
 for k in word:
  dictWord[k] = 1
 start = 0
 for i in arrayfile:
  i = i.replace("\n","")
  if(i == "START"):
   break
  start +=1 
 arrayWord = []
 for x in range(start,len(arrayfile)):
  arrayfile[x] = arrayfile[x].replace("\n","")
  if len(word) == len(arrayfile[x]) :
   dictArry = {}
   for line in arrayfile[x]:
    dictArry[line] = 1
   if dictArry == dictWord:
    arrayWord.append(arrayfile[x])
 if arrayWord != []:
   return sorted(arrayWord)
 else:
   return ""
output = [] 
for line in sets:
 anagram = anagrams(line)
 if len(anagram) > 1 and anagram not in output:
  output.append(anagram)
 if len(sets) == 0:
  break
output = sorted(output)
f = open(filename,"w")
for out in output:
 print(out,file = f)
f.close()
