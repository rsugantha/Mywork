'''
Find the factorial of a given integer 'n' recusively.
(Avoid using Non - recursive factorial funcion as it fails for large inputs)
Input Format
The input contains an integers n.
Output Format
Print n!.
Example 1
Input
3
Output
6
Explanation
3 * 2 * 1 = 6
Example 2
Input
5
Output
120

#recursion
def tri_recursion(k):
  print('call',k)
  if(k > 0):
    print('bt')
    result = k + tri_recursion(k - 1)
    #5+4+3+2+1 1 3 6 10 15
    print(result,k)
  else:
    print('here')
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)

'''

#init
f=0
#input
n=int(input('Enter n:'))

if n>=0:                        #validate input
    def fact(n):
            if n>0:
                f=n*fact(n-1)  #cal factorial recursively
            else: f=1          #factorial of zero is one
            return f
    #eof

    out=fact(n)
    outmsg='Factorial of {} is {}'
    print(outmsg.format(n,out))
else:
    print('Factorial of negative numbers are complex')

