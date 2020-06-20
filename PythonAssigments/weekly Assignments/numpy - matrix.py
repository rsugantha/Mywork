import numpy as np
'''
print(3%2)
even_squares = [a * a for a in range(10) if not a % 2]
print(even_squares)
'''
'''
#a=np.array([[1,2,3],[4,5,6]])
#print(a)
lst = []
n = int(input("Enter number of rows : "))
m = int(input("Enter number of cols : "))
for i in range(0, n):
    ele=[]
    for j in range(0,m):
        ele.append(int(input()))
    lst.append(ele)

print(lst)
a=np.array(lst)                     #array printing
result = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]  #array Transpose
print(result)
print(np.array(result))
#or
print(np.array(lst).transpose())
#**********
print("A[:,0] =",a[:,0]) # First Column
print("A[:,3] =", a[:,2]) # second Column
print("A[:,-1] =", a[:,-1]) # Last Column (4th column in this case)

#print(np.indices((2,2)))
print(np.arange(10))
print(np.linspace(1., 4., 5))
print()
a=[[1,2,3],[4,5,6]]
x = np.arange(6).reshape(2, 3)
y= np.array(a).reshape(2,3)
print(y)
'''
'''
lst = []
n = int(input("Enter number of rows : "))

for i in range(0, n):
    #ele = [input(), int(input())]
    ele = input().split()
    lst.append(ele)

print(lst)
#print(np.asarray(lst))
print(np.array(lst))
'''
'''
# number of elements
n = int(input("Enter number of elements : "))
# Below line read inputs from user using map() function
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is - ", a)
print(np.asarray(a))

'''
'''
#************
lst1 = [int(item) for item in input("Enter the list items : ").split()],[int(item) for item in input("Enter the list items : ").split()]
print(lst1)
print(np.asarray(lst1))
#*************'''
'''
#Multiplication of array
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
#print(C)'''

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
