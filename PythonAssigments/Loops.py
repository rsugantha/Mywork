'''When any photo is uploaded following events may occur:

If any of the width or height is less than S, the user is prompted to upload another one. Print "CHANGE" in this case.
If width and height, both are large enough and
(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.

(b) else user is prompted to crop it. Print "CROP" in this case.

S=input().split()
L=S[0]
W=S[1]
H=S[2]
if(W<L or H<L ):
    print("CHANGE")
elif(H==W):
    print("ACCEPTED")
else:
    print("CROP")

'''
'''Write a program to check whether two strings are anagram of each other or not. 

An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “lion” and “niol” are anagrams of each other.

Input: 

First line of the input is the number of test cases T.

Each test case contains 2 separated strings str1 and str2 

Output: 

Yes - in case the strings are anagrams of each other

No - in case the strings are not anagrams of each other

T=int(input())
out=0
for x in range (T):
    str=input().split()
    str1=str[0]
    str2=str[1]
    #print(str1,str2)
    if(len(str1) != len(str2)):
        out=2
    else:
        for x in range(len(str1)):
           if(str1[x] in str2):
               out=1
           else:
               out=2

    print("Yes") if out==1 else print("No")
    
'''
'''A + (A + B) + (A + 2B) + (A + 3B) + and so on
You are to calculate the sum of N terms of arithmetic sequence.
Input:
The Testcase contains space separated Integers A B N where A is the first value of the sequence, B is the step size and N is the number of terms in the sequence

Output:
For the test case Print the value of the sum of N numbers in the sequence.
out=0
inp=input().split()
A=int(inp[0])
B=int(inp[1])
N=int(inp[2])
for N in range(N):
    x=A+B*N
    out=out+x
print(out)

'''
'''Given 3 Integers L,M,N. Write to program that can identify the median numbers among the triplet ie. Identify the number which is neither the largest nor the smallest

inp=input().split()
L=int(inp[0])
M=int(inp[1])
N=int(inp[2])
HI=LW=ME=0

if(L>M):
    HI=L
    LW=M
else:
    HI=M
    LW=L
if(N>HI):
    ME=HI
    HI=N
else:
    if(N>LW):
        ME=N
    else:
        ME=LW
        LW=N
print(ME)
'''
'''IIT Bombay allocates a 5 Digit Student ID to each student when they take admission into the college.The 2 Left Most digits refers to the Batch Number. Third Digit refers to the Engineering Branch. Last 2 Digits refer to the class roll number. Write a program that prints only the Student Roll Number from the Student ID.

Input:
Each test case contains the 5Digit Student ID

inp=str(input())
RL=inp[3:5]
print(RL)

'''
'''
Harold is building an app that calculates the grade based on the aggregate percentage of a student. The Percentage is computed based on 5 subjects - Physics, Chemistry, Biology, Mathematics and Computer. Help Harold to calculate percentage and grade according to given conditions:

 
If percentage >= 90% : Grade S

If percentage >= 80% : Grade A

If percentage >= 70% : Grade B

If percentage >= 60% : Grade C

If percentage >= 40% : Grade D

If percentage < 40%   : Grade E'''


Tot=0
done=True
ma=input().split()
lm=len(ma)
for x in ma:
    Tot+=int(x)
percentage=Tot/lm
#print(Tot,percentage)
while(done):
    if(percentage < 40):
        print("{:.2f} E".format(percentage))
        done=False
    elif((percentage >= 40) and (percentage < 60)):
        print("{:.2f} D".format(percentage))
        done = False
    elif((percentage >= 60) and (percentage < 70)):
        print("{:.2f} C".format(percentage))
        done = False
    elif((percentage >= 70) and (percentage < 80)):
        print("{:.2f} B".format(percentage))
        done = False
    elif((percentage >= 80) and (percentage < 90)):
        print("{:.2f} A".format(percentage))
        done = False
    elif(percentage >= 90 ):
    #else:
        print("{:.2f} S".format(percentage))
        done = False



