'''Number of 1s
Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.
Example
Input matrix
0 1 1 1
0 0 1 1
1 1 1 1 // this row has maximum 1s
0 0 0 0
Output: 2
If 2 rows have maximum number of ones print the lower index.
Input:
Test case consists of 2 lines .
The first line of test case is are two space separted integers R and C denoting the no of rows and columns of matrix .
Then in the next line are row*col space separated values of the matrix M.
Output:
For each test case in a new line print the required row index
Example 1:
Input:
3 4
0 1 1 1 0 0 1 1 0 0 1 1
Output:
0
Example 2:
Input:
2 2
0 1 1 1
Output:
1
'''

#Inputs
rc = input('Enter the row and column values: ').split()
r = int(rc[0])
c = int(rc[1])
inp=input('Enter the array values: ').split()
l=int(len(inp))

inp=list(map(int,inp))

inpa=[]                             #Input array
for i in range(0,l,c):
    ina = inp[i:i+c]                #creating the sublists (c coloumn)
    inpa.append(ina)

maxc=[]                             #Count of 1's array
c1 = cm = 0
for i in range(int(r)):
    x = inpa[i]
    c1 = inpa[i].count(1)      # count the number of '1' ones in each row
    maxc.append(c1)
    if c1 > cm:                # Finding the maximun no of ones
        cm = c1

#printing the pos of max num of ones(cm) in maxc array
print('The maximum no of one is found at index: ',maxc.index(cm))