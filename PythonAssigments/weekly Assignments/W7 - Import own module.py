'''1. Design your own module Grade : 15
Design a module 'cal.py' to perform simple mathematical calculations like
1. add
2. Subtract
3. multiply
4. divide
with the given numbers .
Also write a python program to import the cal module to perform all the above mentioned calculations
Constraints: For divide the numbers should be non zero
Input:
The operation to be performed from the above list
Space separated numbers
Output:
The result of the operation performed
Example
Input:
1
35 20
Output
55'''

import cal as c                              #importing   CAl module as c

#Inputs
print(' 1.add \n 2.Sub \n 3.Multiply \n 4.Divide')
op = input('Enter the operation :')
n = input('Enter the numbers: ').split()
n = list(map(int,n))
l = len(n)

s = c.calc(n,int(op),l)                     #CAll calc function from cal(c) module

print('The ouput:',s)                       #print output as received
