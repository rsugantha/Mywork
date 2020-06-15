'''Given an array in such a way that the elements stored in array are in increasing order initially and then after reaching to a peak element , elements stored are in decreasing order. Find the highest element.
Input:
The first line of the test case consists of an integer n. The next line consists of n spaced integers.
Output:
Print the highest number in the array.
Example 1:
Input:
11
1 2 3 4 5 6 5 4 3 2 1
Output:
6
Example 2:
Input:
5
1 4 9 4 1
Output:
9

n=input()
na=input().split()

for i in range (int(n)):
    j=i+1
    if na[j] < na[i]:
        print(na[i])
        break
'''
'''
Problem Statement
Given an array, print k largest elements from the array.  The output elements should be printed in decreasing order. Try not to use in-built sort functions
Input:
The first line of the test case is N and k, N is the size of array and K is the largest elements to be returned.
The second line of each test case contains N input C[i].
Output:
Print the k largest element in descending order.
Example 1:
Input:
5 2
12 5 787 1 23
Output:
787 23
Example 2:
Input:
9 3
2 4 8 5 13 16 1 18 6
Output:
18 16 13

nk=input().split()
N = int(nk[0])   #size of array
K = int(nk[1])    #no.of outputs required
C = input().split()

j = 1
temp=0

#Sort
for i in range(int(N)):
    for j in range(int(N) - 1):
        if (int(C[i]) < int(C[j])):
            j += 1
        else:
            temp = C[i]
            C[i] = C[j]
            C[j] =  temp
for i in range(K):
    print(C[i],end=' ')
'''

'''Problem Statement
Given an array of N integers. Your task is to write a program that returns the maximum value of ∑arr[i]*i, where i = 0, 1, 2,…., n – 1.
Note : You are allowed to rearrange the element of the array. Try not to use inbuilt sort functions
Input:
First line of the test case contains an integer N, denoting the size of the array. Next line contains N space separated integers denoting the elements of the array.
Output:
For each test case print the required answer on a new line.
Example 1:
Input:
4
3 5 6 1
Output:
31
Example 2:
Input:
5
4 6 2 3 5
Output:
50
Explanation
Testcase 1
Input : N = 4, 
arr[] = { 3, 5, 6, 1 }
Output : 31
If we arrange arr[] as { 1, 3, 5, 6 }. 
Sum of arr[i]*i is 1*0 + 3*1 + 5*2 + 6*3 = 31, which is maximum

Testcase 2
Input : N = 5, 
arr[] = { 4, 6, 2, 3, 5 }
Output : 46
If we arrange arr[] as { 2, 3, 4, 5, 6 }. 
Sum of arr[i]*i is 2*0 + 3*1 + 4*2 + 5*3 + 6*4 = 50, which is maximum


N = input()
arr= input().split()
sumarr=0
for i in range(int(N)):
    for j in range(int(N) - 1):
        if arr[i] < arr[j]:
            temp=arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range (int(N)):
    sumarr += int(arr[i]) * i
print(sumarr)
'''
'''Problem Statement
Given an array of integers (both odd and even), the task is to sort them in such a way that the first part of the array contains odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order. Try not to use inbuilt sort functions
Examples:
Input  : A[] = {1, 2, 3, 5, 4, 7, 10}
Output : A[] = {7, 5, 3, 1, 2, 4, 10}
Input:
The test case contains an integer N denoting the size of the array. The next line contains N space separated values of the array.
Output:
For each test case in a new line print the space separated values of the  new transformed array.
Sample Input:
7
1 2 3 5 4 7 10
Sample Output:
7 5 3 1 2 4 10

N=input()
A=input().split()

def sortA(arr,N,op):
    for i in range(int(N)):
        for j in range(int(N) - 1):
            if op == 'A':
                if arr[i] < arr[j]:
                    temp=arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
            else:
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
    return arr

#sortarr = sortA(A,N,'D')
#print(sortarr)
evnarr=[]
oddarr=[]
for i in range(int(N)):
    if int(A[i]) % 2 == 0:
        evnarr.append(int(A[i]))
    else:
        oddarr.append(int(A[i]))

print(evnarr)
print(sortA(evnarr,int(len(evnarr)),'A'))
print(oddarr)
print(sortA(oddarr,int(len(oddarr)),'D'))

sortarr= sortA(oddarr,int(len(oddarr)),'D') + sortA(evnarr,int(len(evnarr)),'A')
print(sortarr)

for i in range(int(len(sortarr))):
    print(sortarr[i],end=' ')

'''
'''Given a number N, you have to find nearest prime number. If there are more then one, print the smaller one.
Input:
Only line of test case contains one integers N, as described above.
Output:
For each test case output a single line containing one integer, the answer to the above problem.
Example 1:
Input:
14
Output:
13
Explanation:
Test case 1 - for 14, nearest prime number is 13
Example 2:
Input:
100
Output:
101
Explanation:
Test case 1 - for 100, nearest prime number is 101'''

N=input()
n = p = i =0
k = 1
primenotfound = True
while primenotfound:
    i = int(N) - k
    if (i % 2  == 0) or (i % 3 == 0):
            k +=1
    else:
        n = i
        primenotfound = False
#print(n)

primenotfound = True
k = 1
while primenotfound:
    i = int(N) + k
    if (i % 2 == 0) or (i % 3 == 0):
        k += 1
    else:
        p = i
        primenotfound = False
#print(p)

#Finding nearest

def near(p,n,N):
    if (N-n) > (p - N):
        return p
    elif (N-n) < (p - N):
        return n
    elif (N-n) == (p - N):
        return n

out=near(int(p),int(n),int(N))
print(out)
