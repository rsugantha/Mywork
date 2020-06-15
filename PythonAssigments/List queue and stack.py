'''
Problem Statement
Complete the function insertAtBeginning() which inserts the data in front of the linked list and insertAtEnd() which appends the data at the end of the linked list.
With each input there will be an extra boolean variable that chooses from where to insert the data.
0 - Insert at Beginning
1 - Insert at End
Input:
The 1st line of input contains the N -number of nodes to be inserted to the link List.
The 2nd line contains 2N space separated integers. Each Element followed by its boolean variable(0 or 1)
Output:
For each test case output will be the linked list after inserting all the elements.

Example:
Input:
5
8 0 5 1 6 1 2 0 7 0
Output:
7 2 8 5 6

#init
olist=[]
count = 0
i = 0
j = 1

#inputs
N=input()
inp = input().split()
print(inp)

def insertAtBeginning(n):
    olist.insert(0,n)

def insertAtEnd(n):
    olist.append(n)

while count < int(N):
    #print(count)
    #print(inp[i], j)

    if (int(inp[j]) == 0 ):
       insertAtBeginning(int(inp[i]))
    else:
       insertAtEnd(int(inp[i]))

    count += 1
    i = i + 2
    j += 2

print(olist)

for i in range (len(olist)):
    print(int(olist[i]),end=' ')

'''
'''Problem Statement
You are provided an input consisting of N queries. Each query is one of these three types:
1 n  -Push the element n into the stack.
2     -Delete the element present at the top of the stack.
3     -Print the maximum element in the stack.

Input Format
The first line of input contains an integer N. The next  n lines each contains a query of the above mentioned format.
Output Format
For each type 3 query, print the maximum element in the stack on a new line.

Example 1:
Input
6
1 9
1 11
2
3
1 15
3

Output
9
5

Example 2:
Input
5
1 5
1 10
2
3
1 10
Output
5'''
'''
N=input()
lista=[]

def pushst(a):              #Push the integer into stack
    lista.append(a)

def popst():                #remove the top integer in stack
    lista.pop()

def maxst():                #print the max integer in the stack
    print(max(lista),end='\n')

for i in range (int(N)):
    n=input().split()
#    print(i,n)
    q = int(n[0])
    if    q == 1:  pushst(int(n[1]))
    elif  q == 2:  popst()
    elif  q == 3:  maxst()
#    print(lista)

'''

'''Problem Statement
All values stored within a computer exist as a string of binary digits, a string of 0s and 1s. Given a Decimal Integer N ( base 10), write a program that converts the Decimal Integer to a Binary Number(Base 2)
Input:
The Input contains a decimal number N
Output:
Output the Binary equivalent of the Decimal number

Example 1:
Input:
3
Output:
11

Example 2:
Input:
233
Output:
11101001

N = input()
n= int(N)
lst=[]

if   n == 1: print('1')
elif n == 0: print('0')
else:
    while n != 1:
        R = n % 2
        Q = n // 2
        lst.append(int(R))
        n = Q
    lst.append(n)
    lst.reverse()
    for i in range(len(lst)):
        print(lst[i],end='')
'''
'''
Problem Statement

Given an input integer N, write a program that reads the number and removes consecutive digits that are repeated.
 Ex : If the Input is 51115. In this case the digit 1 has consecutive occurrences of 1. Hence we remove the consecutive occurring ones such that the output is 515
Input:
Each test case contains the integer N.
Output:
Print the number after removing consecutive digits
Constraints:
1<= N <=1018
Example 1:
Input:
46224554
Output:
462454
Example 2:
Input:
599551
Output:
5951


N=input()
lst=[]
i=0
j=1

lst.append(N[0])
for i in range(1,len(N)):
    ln= len(lst) - 1
    if lst[ln] == N[i]: continue
    else:
        lst.append(N[i])
for i in range(len(lst)):
        print(lst[i],end='')
'''

'''
Write a program where you must first implement a queue using two stacks. Then process queries, where each query is one of the following types:

1 n - Enqueue element n into the end of the queue. (1 and n are space separated)

2 - Dequeue the element at the front of the queue.

3 - Print the element at the front of the queue

 

Input

The first line contains a single integer Q, denoting the number of queries. 
Following Q lines contain a query of any of the following types as mentioned above.
Output
For each query of type 3, print the value of the element at the front of the queue in a new line.
Example 1:
Input
8
1 5
1 8
2
1 4
3
1 28
2
3
Output
8
4
'''

Q=input()
lista=[]

def pushq(a):              #Push the integer into Q
    lista.append(a)

def popq():                #remove the front integer in Q
    lista.pop(0)

def maxq():                #print the max integer in the Q
    print((lista[0]),end='\n')

for i in range (int(Q)):
    n=input().split()
#    print(i,n)
    q = int(n[0])
    if    q == 1:  pushq(int(n[1]))
    elif  q == 2:  popq()
    elif  q == 3:  maxq()
#    print(lista)




