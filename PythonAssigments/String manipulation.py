S=input()
l=len(S)
count=0
listA=list()
listB=list()
if (1 <= l<= 100):
  for i in range(l):
    for j in range(i+1,l+1):
        a=S[i:j]
        listA.insert(i,a)
        count=count+1
       # print(count)
#print(listA)

#listB.append('mamalayalamam')
  for i in range(count):
    b=listA[i]
    c=b[::-1]
    if(b==c):
        listB.insert(i, c)

if listB == []:
    print(S[0])
else:
  #  print(listB)
    print(max(listB,key=len))
'''#Given a string S, find the longest palindromic substring in S
S='abc'
l=len(S)
maxl=0
count=0
listA=list()
listB=list()
if (1 <= l<= 100):
  for i in range(l):
    for j in range(i+1,l):
        a=S[i:j]
        listA.insert(i,a)
        count=count+1
       # print(count)
#print(listA)

#listB.append('mamalayalamam')
  for i in range(count):
    b=listA[i]
    c=b[::-1]
    if(b==c):

        lp=len(b)
        if(lp>maxl):
            out=b
            p=out
            maxl = lp

        elif(lp==maxl):
            print(b,p)
            out=p

        #listB.insert(i, c)
#print(listA)
if(out==''):
    print(S[0])
else:
    print(out)
if listB == []:
    print(S[0])
else:
  #  print(listB)
   # if (len(listB[0]))
    print(max(listB,key=len))'''

'''
str= input('Enter the string:')
s=str[0]
if(s.isupper()):   #check whether  first character is upper or lower case
    print(str.upper())
else:
    print(str.lower())


Problem statement 1:
Given a string S, the task is to change the string according to the condition; 
If the first letter in a string is capital letter then change the full string to capital letters, else change the full string to small letters.

Input:
The test case contains a string S.

Output:
For the test case, print the changed string in a new line.

Example 1:

Input:

boOTcamP

Output:

bootcamp

Example 2:

Input:

XoBIn

Output:

XOBIN
'''

'''
Problem statement 2:
Given a String of length N, write a program to reverse the words in it.

Input:
Each testcase contains a string containing spaces and characters.
 

Output:
For each test case, output a single line containing the reversed String with words in reverse order.
Constraints:
1<=Length of String<=2000

Example:
Input:
i like this program very much
Output:
much very program this like i
'''
'''
#str=input('enter the string:')
str='i like this program very much'
a=str.split()
#print(a[2])
l=len(a)
if(1<=l<=2000):    #given constraint
    while(l>0):    #flipping using while
        print(a[l-1],end=' ')
        l=l-1

'''