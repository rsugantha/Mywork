'''
Matrix Transpose
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
1 3 5'''

#init
c=[]

#inputs
A=input('Enter m and n:').split()
m=int(A[0])
n=int(A[1])

print("enter array elements:")
for i in range(m):
    a = []
    for j in range(n):                  #create input matrix
        a.append(int(input()))
    c.append(a)

print('input matrix:')
for i in range(m):
    for j in range(n):
        print(c[i][j], end = " ")      #print ip elements in matrix format
    print()

print('output matrix:')
for i in range(n):                      #create transpose
    for j in range(m):
        print(c[j][i],end= ' ')
    print()
