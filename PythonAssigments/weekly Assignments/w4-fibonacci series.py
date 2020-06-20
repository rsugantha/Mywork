'''
Write a program to generate nth term of the Fibonacci series.
Fibonacci series is a series of numbers in which each number ( Fibonacci number</em> ) is the sum of the two preceding numbers.
The simplest is the series 1, 1, 2, 3, 5, 8,.. .
Input Format
The input consists of a single integer.
Output Format
Output is an integer that is the nth term of the fibonacci series.
Sample Input
5
Sample Output
5
Explanation
5th term of the fibonacci series is 5
1 1 2 3 5(5th term)...

1+0 1+1
'''

#init
i=c=0
f=[]
opmsg='The value at the position of {} is {}'

#input
n=input('Enter the value of n: ')
a=input('Enter the first value of fibonacci series:')
b=input('Enter the second value of fibonacci series:')

f.insert(0,int(a))
f.insert(1,int(b))
print('First two values in series:',f)

#calculate fibonacci series using recursive function
def fibo(n,a,b):
    while(n>0):
        c=int(a)+int(b)
        f.append(c)
        a=b
        b=c
        fibo(n-1,a,b)
        return(f)
#eof

if (int(n)<=0):
    print('Enter valid input')                  #check for valid input
elif(int(n)<=2):
    print(opmsg.format(n,f[int(n)-1]))          #Directly print the values for first two position
else:
    fb=fibo(int(n),int(a),int(b))               #Call fibo function

    print('The fibonacci series for given input :',fb)      #print outputs
    print(opmsg.format(n, f[int(n) - 1]))
