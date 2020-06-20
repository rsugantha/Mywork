'''Sum of elements Grade : 10
Calculate sum of first 5 elements in the given array
Input
N : Number of elements
A : Space separated array elements
Output
If number of elements is less than 5 then print "Index out of range! Can not calculate the sum",
otherwise print the addition of first 5 elements
Example
Input
7
10 20 30 40 50 60 70
Output
150
Example
Input
3
11 22 33
Output
Index out of range! Can not calculate the sum'''

N = input("Enter the number of elements: ")
A = input("Enter Space separated array elements: ").split()

s = 0
try:
    if int(N) < 5 or len(A) < 5:                                #Check if N or number of elements entered is less than 5
        raise IndexError                                        #Throw index error
except IndexError:
    print("Index out of range! Can not calculate the sum")
else:
    for i in range(5):                                          #Else calculate and print sum
        s += int(A[i])
    print("Sum of elements: ",s)