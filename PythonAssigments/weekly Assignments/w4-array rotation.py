'''Given an array, right rotate an array by one, ie. shift all elements to the right by 1 place.
Input:
The first line of test case contains an integer n denoting the size of the array.
Then following line contains 'n' integers forming the array elements.
Output:Output the cyclically rotated array by one.
Example 1:
Input:
5
1 2 3 4 5
Output:
5 1 2 3 4
Example 2:
Input:
6
6 10 4 2 1 7
Output:
7 6 10 4 2 1'''

#init
newarr=[]
#inputs
n=input('Enter the length of array: ')
arr=input('Enter the array elements: ').split()

#Take the last element of array and create new array
f=(arr[int(n)-1])
newarr.append(f)

#Add the rest of the array elements
for i in range(int(n)-1):
    fn=arr[int(i)]
    newarr.append(fn)
print('Rotated array: ',newarr)