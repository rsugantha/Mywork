'''Sum Of Array
Given an integer array of size N, Write a Program to find sum of elements in it.
Input:
The First Line of the Testcase contatain an Integer N Denoting the size of array.
The nextline of the testcase contains N space separated integers.
Output:
Print the sum of all elements of the array of the testcase
'''

#init
sa=0

#inputs
N=input('Enter size of array:')
i1=input('Enter array:').split()


if int(N)>0:        #validate input
    print('performing sum of array')
    for i in range(int(N)):
        sa += int(i1[i])  # adding array elements one by one
    print("sum of array:", sa)
else:
    print("Invalid array length")



