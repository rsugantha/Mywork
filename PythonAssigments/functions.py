'''Given an integer N, find sum of all digits of N.
Input:
The testcase containts an integer N.
Output:
Calculate the sum of digits of N.
Example 1:
Input
34
Output
7
''
def sumtn(num):
    sum = 0
    for i in range(len(num)):
          sum+=int(num[i])
    return(sum)
#eof

num=input()
print(sumtn(num))
'''

'''Marks of Students in the Class Test is stored in an Array. Given an array of Integers, find the highest marks of students in the clas test

Input:
The First line of the test case contains an integer n , denoting the number of elements in the array. Then next line contains those n space separated integers of the array.

Output:
Print the maximum element in the array.

Example:
Input:
5
9 34 45 87 89

Output :
89''

def maxmark(marklist):
    return max(marklist)

mark=input().split()
marklist=list(map(int,mark))
print(maxmark(marklist))

'''

'''Problem Statement
CM Arvind Kejriwal begins experimenting with the Odd-Even Rule in Delhi. The Rule states that only cars with Even Number plates can ride only on Even Dates while Odd Number Plates can Ride only on Odd Dates. In case a car is driven on the wrong day it is fined. Different police officers collect different fines arbitarily depending on the size of the car

Given an array of Car Numbers, an array of Fine-Value and the date, Write a program to find the total fine which will be collected on the given date. 

Input:
The test case consists of three lines.
First line contains two space separated integers N(Size of Array) & Date. Second line contains N space separated Car Numbers. Third line contains N space separated Fine-values

Output:
Calculate the Total Fine collected on the particular date.

Constraints:
1000<= Car Number<=9999
1<=Fine<=1000
1<=Date<=31

Example:
Input:
6 8
6767 8430 2375 7682 2325 2352 
100 200 250 500 350 200

Output:
700

ND=input().split()
N=int(ND[0])    #No of cars
D=int(ND[1])    #Date

car=input().split()
fine=input().split()

def calfine(day,car,fine):
    amt=0
    if (D%2 ==0):
        for i in range(N):
            if int(car[i]) %2 != 0:
                amt=amt+int(fine[i])

    else:
        for i in range(N):
            if int(car[i])%2 == 0:
                amt=amt+int(fine[i])

    return amt
#eof

print(calfine(D,car,fine))
'''
'''
Write a program to find the hypotenuse of a right angled triangle when 2 sides of the triangle are given.
Input:Input consists of 2 space separated positive numbers denoting the two sides of the right angled triangle.

Output:Output consists of the value of hypotenuse rounded off to one decimal.

Example 1:
Input
3 4
Output
5.0
Example 2:
Input
5 6

Output
7.8


AB=input().split()
ABint= list(map(int,AB))

def hypo(x):
    C=(ABint[0]**2 + ABint[1]**2)**(1/2)
    return float(C)

hyp=hypo(ABint)
print('%.1f'%hyp)

'''
'''Susan and Gabby like to sum up the money they saved in summer vacations and go to the toy store every year. Susan never buys the same toy that Gabby does as they play together and prefer variety of toys. And they tend to spend all their money while buying toys.

Given a list of prices of toys available at the toy store, select the two toys that will cost all of the money they have.

Input Format
Input consists of three lines,
First line has an integer value k, denoting the amount of money both of them have.(Combined)
Second line has an integer value n, denoting number of toys available at the store.
Third Line has n values each denoting the price of the toys present in the store.
Output Format
Output should print the positions of the toys that susan and gabby buy as space seperated values.
Example 1
Input
6
5
1 2 3 4 5
Output
1 5
Explanation
Susan and Gabby Buy toys costing 1 and 5 respectively at positions 1 and 5 in the store.
toys costind 2, 4 can also be bought but the first occuring combination is considered.

Example 2
Input
7
8
1 2 6 7 13 15 17 19
Output
1 3'''

k=int(input())  #amt
n=int(input())   #no of toys
price=input().split()   #price of toys
pl=list(map(int,price))
i=j=0

def findsum(a,b):
    print(a,b)
    if pl[a]+pl[b] == k:
        print('mat found')
        return (1)
    else: return (0)


while(i<n):
     j=i+1
     while(j<n):
        x=0
        x= findsum(i,j)
        if x ==1:
            print(i+1,j+1,end=" ")
            break
        else: j+=1
     if x==1: exit()
     else:i+=1



