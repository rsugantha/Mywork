'''1. Relative sorting
Given two array A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those in A2.
For the elements not present in A2. Append them at last in sorted order.
It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all
distinct elements. Note : Try not to use in-built sort functions
Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
A2[] = {2, 1, 8, 3}
Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
Since 2 is present first in A2[], all occurrences of 2s should appear first in A[], then all occurrences 1s as 1 comes after 2 in A[].
Next all occurrences of 8 and then all occurrences of 3. Finally we print all those elements of A1[] that are not present in A2[]
Input:
The first line of input denotes number of test cases,
The first line of each test case is M and N. M is the number of elements in A1 and N is the number of elements in A2.
The second line of each test case contains M elements. The third line of each test case contains N elements.
Output:
Print the sorted array according order defined by another array.
Example 1:
Input:
1
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
Output:
2 2 1 1 8 8 3 5 6 7 9
Example 2:
Input:
1
4 2
1 4 7 2
4 2
Output:
4 2 1 7'''
'''

#Method1: Reads the input array twice. So i have revised it in method 2 to read Input array only once:

#inputs
T = input('Enter the no of Test cases:')

#create outputs for test cases one by one
for i in range(int(T)):
    mn = input('Enter the length of array 1 and 2: ').split()
    M  = int(mn[0])
    N  = int(mn[1])
    A1 = input('Enter the A1 Array: ').split()
    A2 = input('Enter the A2 Array: ').split()

    #Create a new array with the matching elements of A1 and A2
    newarr = []        #output array
    for j in range(N):
       for i in range (M):
            if A1[i] == A2[j]:
                newarr.append(A1[i])

    print(newarr)

    n=len(newarr)
    print(n)
    for i in range (M):                     # loop for finding the unmatched elements from A1
        if A1[i] not in A2:
            nn=len(newarr)
            print(A1[i],nn)
            if n == nn:                     # Check if newarr length has changed or not( to see if its first unmatched entry )
                print('first')
                newarr.append(A1[i])        # Appending the first unmatched element at the end of newarray
                print(newarr)
    
            else:
                if A1[i] > newarr[nn-1] or A1[i] == newarr[nn-1]:      #Sorting and inserting the other unmatched elements
                        newarr.insert(nn+1,A1[i])
                else:
                    for j in range(n,nn-1):
                        print(A1[i] , newarr[j])
                        if A1[i] < newarr[j]:
                             newarr.insert(j,A1[i])
    print('The ouput :' ,newarr)
'''






# Method2: Improved the logic to Read the input array only once

# input No of test cases
T = input('Enter the no of Test cases:')

# create outputs for test cases one by one
for i in range(int(T)):
    #Inputs
    mn = input('Enter the length of array 1 and 2: ').split()
    M = int(mn[0])
    N = int(mn[1])
    A1 = input('Enter the A1 Array: ').split()
    A2 = input('Enter the A2 Array: ').split()

    #Function to Sort and insert unmatched elements:
    def unmatchin(x):
        nn = len(newarr)
        if p == nn:               # Check if newarr length has changed or not( to see if its first unmatched entry )
            newarr.append(x)      # Appending the first unmatched element at the end of newarray
        else:
            if x > newarr[nn - 1] or x == newarr[nn - 1]:  #Inserting unmatched element which is > or == to previous unmatched element
                newarr.insert(nn + 1, x)
            else:
                for j in range(p, nn - 1):                  #Inserting unmatched element which is lesser than the previous unmatched element
                    if x < newarr[j]:                       #at its correct position
                        newarr.insert(j, x)


    # Main loop
    newarr = []  # output array
    p = 0        # Position of matched inserts

    for j in range(N):                                      # Read arrays
        for i in range(M):
            if A1[i] == A2[j]:                              # Insert the matched elements in Output array
                newarr.insert(p, A1[i])
                p +=1
            elif A1[i] not in A2 and A1[i] not in newarr:   # Call fun for unmatched elements which is not yet inserted into out array
                unmatchin(A1[i])

    print('The output array: ', newarr)
