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
'''

#init
opar=[]

#inputs
A=input('Enter the size of array and no of command:').split()
n=int(A[0])    #size of array
c=int(A[1])    #commands=no of exceution

for i in range(n):  #create an empty op array
    opar.append(0)
print(opar)

for j in range(c):
   B=input('Enter l ,r and value:').split()   #receive l,r and value
   l=int(B[0])
   r=int(B[1])
   v=int(B[2])
   for k in range(l,r+1):                     #add value v in the range of l and r
       opar[k]+=v
print(opar)
