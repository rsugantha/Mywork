inp = input('Enter a number: ')
I=int(inp)
Fac = 1
for i in range(1,I + 1):
  	Fac= Fac * i
  	if (Fac <= I):
  		print(Fac, end=" ")


"""
Problem statement:
An Integer I is called a factorial number if it is the factorial of a positive integer. The First few Factorial Numbers are 1,2,6,24

(0! =1 1!=1 2! =2   3!= 6).
Given a number I, Write a Program that prints all factorial numbers less than or equal to I.
Input:
Each test cases contains an Integer I.

Output:
For each test case, print all the space separated factorial numbers smaller than or equal to I.

Example 1:

Input
10


Output
1 2 6

Example 2:

Input
25


Output
1 2 6 24

"""