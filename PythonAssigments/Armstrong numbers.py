N=input()
l=len(N)
#print('l:',l)
ar=0
n=0
while(n < l):
    a=int(N[n])
    ar=ar+a**l		#armstrong calculation
    #print('ar:',ar)
    n=n+1

if (ar==int(N)):	#cheking if armstromg is same as input
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

'''
Problem statement:
Write a program to find whether the given number ‘N’, is an Armstrong number or not.

An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.

Input:

Input consists of an integer 'N'.

Output:

Output should print “Armstrong Number” or “Not Armstrong Number”.

Example 1:

Input

371

Output

Armstrong Number

Explanation

371 is an Armstrong number since 3 ^ 3 + 7 ^ 3 + 1 ^ 3 = 27 + 343 + 1 = 371.

 

Example 2:

Input

400

Output

Not Armstrong Number

'''