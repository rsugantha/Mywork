'''Sum Of Array
Given an integer array of size N, Write a Program to find sum of elements in it.
Input:
The First Line of the Testcase contatain an Integer N Denoting the size of array.
The nextline of the testcase contains N space separated integers.
Output:
Print the sum of all elements of the array of the testcase
'''
sa=0
N=input()
i1=input().split()
for i in range(int(N)):
    sa+=int(i1[i])
print("sum of array:",sa)

'''
Array Manipulation
Starting with an array of zeros, for each command add the given value to all the array element in the given interval (l, r) inclusive of both l and r. Print the final array.
Input Format
The first line contains two space-separated integers n and c, denoting the size of the array and the number of commands. Each of the next lines contains three space-separated integers l, r and value, the left index, right index and the value to be added.
Output Format
Print the final array.
Example 1
Input
5 3
0 1 100
1 4 100
2 3 100
Output
100 200 200 200 100

A=input().split()
n=int(A[0])    #size of array
c=int(A[1])    #commands=no of exceution
opar=[]
for i in range(n):  #create op array
    opar.append(0)
print(opar)

for j in range(c):
   B=input().split()   #receive l,r and value
   l=int(B[0])
   r=int(B[1])
   v=int(B[2])
   for k in range(l,r+1):
       opar[k]+=v
print(opar)
'''

'''3. Extract The Number
Bharat is given a string that contains text and numbers.
Bharat needs to extract the number from the string such that the number must not contain the integer 9.
NOTE: In case there any multiple numbers that match the condition, Print all numbers in a space separated format( in same order that they appear in the string)
For eg if the string contains "My pin code is 560047 and phone number is 98998" ,
Bharth only needs to extract 560047 and not 98998.
You need to help him extract the number.
Input:
The testcase consists of a String
Output:
Output the extracted number.
Example:
Sample Input 1:
This is alpha 5057 and 97
Sample Output 1:
5057
Sample Input 2:
I have 2 numbers 400 and 380
Sample Output 2:
2 400 380

str=input().split()
for i in range(len(str)):
    if(str[i].isnumeric()):
        if(str[i].rfind("9") < 0):
            print(str[i],end=' ')

'''
'''Matrix Transpose
Given a matrix, print its transpose value.
Input
First line denotes m, n next m lines contain n values each denoting m x n matrix
Output
Output should contain the transpose of the input matrix
Example 1:
Input
3 2
1 2
3 4
5 6
Output
1 3 5
2 4 6
Example 2:
Input
3 1
1
3
5
Output
1 3 5

A=input().split()
m=int(A[0])
n=int(A[1])
c=[]
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    c.append(a)

print('input matrix:')
for i in range(m):
    for j in range(n):
        print(c[i][j], end = " ")
    print()

print('output matrix:')
for i in range(n):
    for j in range(m):
        print(c[j][i],end= ' ')
    print()
    
    '''