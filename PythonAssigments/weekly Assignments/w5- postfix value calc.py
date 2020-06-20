'''2. Value of postfix expression
Suppose you are provided with an input of a postfix expression. Write a program
to evaluate the postfix expression and print its value.
Input:
The test case contains a postfix expression.Operators and Operands are NOT
space seaprated.
Note : You may assume that the Postfix expression in the testcases is valid
Output:
Output the value of the postfix expression.
Constraints:
1 <= length of expression <= 100
Example 1:
Input:
481*+3-
Output:
9
Example 2:
Input:
51*3+
Output:
8'''


ip=input()      #Receive postfix experssion
l=len(ip)
out=[]          #ouput stack

#function to calculate expressions
def calc(x,y,op):
    if    op == '+':  return x + y
    elif  op == '-':  return x - y
    elif  op == '*':  return x * y
    elif  op == '/':  return x / y
    elif  op == '^':  return x ^ y
    elif  op == '%':  return x % y
#eof

for i in range(int(l)):
    op = ip[i]
    if ip[i].isnumeric():               #insert numeric values to op stack as it is
        out.append(int(op))
    else:                               #in case of operand - pop last two values and do calculation
        y=out.pop()
        x=out.pop()
        z= calc(int(x),int(y),op)
        out.append(z)
print(out)

'''
# ***** Program for multi digit Postfix expression******#
#on receiving the input as space separated values ,above program will work for multi digit as well
# 5 88 1 * + 13 -  = 80

ip=input().split()      #Receive postfix experssion as space seprated inputs
l=len(ip)
out=[]                  #ouput stack

#function to calculate expressions
def calc(x,y,op):
    if    op == '+':  return x + y
    elif  op == '-':  return x - y
    elif  op == '*':  return x * y
    elif  op == '/':  return x / y
    elif  op == '^':  return x ^ y
    elif  op == '%':  return x % y
#eof

for i in range(int(l)):
    op = ip[i]
    if ip[i].isnumeric():               #insert numeric values to op stack as it is
        out.append(int(op))
    else:                               #in case of operand - pop last two values and do calculation
        y=out.pop()
        x=out.pop()
        z= calc(int(x),int(y),op)
        out.append(z)
print(out)

'''