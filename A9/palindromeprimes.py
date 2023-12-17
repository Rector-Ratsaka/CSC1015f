#A programme ’ that uses recursive functions to find all palindromic primes between two integers N, M, supplied as input. (start and end points are included).
#Rector Ratsaka
#27 April 2022

import sys
sys.setrecursionlimit (30000)
def funcprime(a,div=2):
    if a%div==0:    return False
    elif div==(a-1):    return True
    else: return funcprime(a,div+1)
        
def palindrome(string):
    if len(string)<=1:
        return True
    return string[0]==string[-1] and palindrome(string[1:-1])
def palindromeprime(N,M):
    if N ==2: print(N)
    #elif N == 3: print(N)
    if 2<=N<=M and funcprime(N) and palindrome(str(N)):
        print(N)
        return palindromeprime(N+1,M)
    elif N<=M: 
        return palindromeprime(N+1,M)
    
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palindromeprime(N,M)

    
 