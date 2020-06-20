'''Evaluate expression Grade 15
You are given a file which contains calculations to perform . The operations which may be requested are limited to addition, subtraction, multiplication, and division.The file will also contain numbers to perform the calculations with
Given :
A text file math_expression.txt
5
6
+
2
*
3
-
4
/
The computation of the above file would look like;
(((5+6)*2)-3)/4'''

#Open the file in Read
mf = open('math_expression.txt','r')
ta = mf.read().split()                   #Read the file into array

def calc(x,y,op):                        #Calulation
    if    op == '+':  return x + y
    elif  op == '-':
        if x > y:     return x - y
        else    :     return y - x
    elif  op == '*':  return x * y
    elif  op == '/':  return x / y
    elif  op == '^':  return x ^ y
    elif  op == '%':  return x % y
#eof


tn = []
for x in ta:                                    #Read and process the integers and Symbols respetively
    if x.isnumeric():
        tn.append(int(x))
    else:
        op = x
        a = tn.pop()
        b = tn.pop()
        c = calc(int(a),int(b),op)
        tn.append(c)

print('The ouput :',tn)
mf.close()                                      #close file