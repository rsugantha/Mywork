#Problem Statement
#Given a String S, find the size of the smallest substring in S which will contain all the distinct characters of the String

#S='SEASHELLSONSEASHORE'
S='SEASHELLSONSEASHORE'
ls=len(S)
count=0
lista=[]
ss=Dist=''
for i in range (ls):     #finding distinct char in string
    if(S[i]  in Dist):
      count=count+1
    else:
      Dist=Dist+S[i]

#print('dist',Dist)

for i in range(ls):     #substring calc
    for j in range(i,ls):
        ss=S[i:j+1]
        if(len(ss)>=len(Dist)):   #adding only if the len of ss = len of distinct characters
             lista.append(ss)
#print('ss',lista)

def lenFunc(e):
  return len(e)

lista.sort(key=lenFunc)    #sorting the substring by len

m=n=i=j=0
while(i<len(lista)):
    out=0
    A=lista[i]
    ll=len(A)
    ld=len(Dist)
    m=n=0
    while (m < ld and n < ll):
        if (Dist[m] == A[n]):
            out=out+1
            m=m+1
            n=0
        else:
            n=n+1
#    print('out',out,Dist)

    if (out==len(Dist)):
        print(len(A),A)
        break
    i=i+1

'''
A="ABDUENX"
B="CBHUEX"
la=len(A)
lb=len(B)
ss=''
m=n=f=0

while(m<la and n<lb):
    if(A[m]==B[n]):
        f=n
        ss=ss + A[m]
        #print(ss)
        m=m+1
        n=n+1
        #print('f',f)
    else:
        n=n+1
#    print(m,n)
    if(n==lb):
       # print('sw')
        m=m+1
        n=f
print(len(ss))
'''
"""
Given two strings, find the length of the longest common substring. A substring here, need not be contiguous but has to appear in the same relative order.

For example “B”, “BA”, “BAD”, “BC”, “AD” are a few substrings of “BACD”.


Input Format

Input consists of two strings A and B.

Output Format

Output should have the length of the longest common substring that A and B have.

Example 1:

Input

BATD ABACD

Output

3

Explanation

The longest common substring is “BAD” for the strings “BATD” and “ABACD”.

The length of ”BAD” is 3

Example 2:

Input

ABDUENX CBHUEX

Output

4

Explanation

The longest common substring is “BUEX” for the strings “ABDUENX” and “CBHUEX”.

The length of ”BUEX” is 4"""


"""
a = "forest"
b = "stfore"
lb=len(b)
p=lb-2
c=b[0:p]
d=b[p:lb]
e=b[0:2]
f=b[2:lb]
a1=d+c
a2=f+e
if (a1==a) or (a2==a):
    print(1)
else:
    print(-1)

print(a1,c,d)
print(a2,e,f)


Given 2 strings Str1 and Str2, the task is to find if a String Str1 can be obtained by rotating another Str2 by two places either clockwise or anti-clockwise.

Examples:

Input : a = "forest" 
        b = "restfo"  // rotated anti-clockwise
Output : 1

Input : a = "forest"
        b = "stfore"  // rotated clockwise
Output : 1

Input:
The Testcase consists of 2 line-separated strings Str1 and Str2.

Output:
For the test case, print 1 if the string Str1 can be obtained by rotating string Str2 by two places. Else print 0.

Example:
Input:
forest
restfo

Output:
1


inp=input()
pat=input()
if(pat in inp):
    print('1')
else:
    print('-1')


Problem Statement
Given a text and a pattern, Find whether the pattern exist in the text or not. If it is present print 1 else print -1

Input:
The test case consist of a string in 'lowercase' only

Output:
Print 1 or -1

Constraints:
1 ≤ |size of String| ≤ 100

Example 1:
Input
Bootcampxobinaokgo
xobin

Output
1

Example 2:
Input
Bootcampxobinaokgo
interact

Output
-1
"""