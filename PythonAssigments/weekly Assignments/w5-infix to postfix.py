'''
1. Infix to postfix
Infix notation are easy for humans to read, while postfix notation is simpler
for machine to understand and parse. This is because such a notation has no
confusion regarding operator precedence. Suppose you are provided an infix
expression. Write a program to convert the infix expression to postfix
expression.
Remember – Order of precedence is BODMAS(Brackets, Orders, Division and Multiplication, and Addition and Subtraction)
Infix Notation:The expression is of the form A op B. An operator op is in-
between every pair of operands a and b
Postfix Notation:The expression is of the form a b op. An operator op follows
the pair of operands a and b
Input:
The first line contains the infix expression. The expression may contain some
or all operator such as ^,*,/,+,-. No spaces between the operator and operands
Output:
Output the postfix expression corresponding the infix expression.
Constraints:
1<=length of expression<=30
Example 1:
Input:
A*(B+C)/D
Output:
ABC+*D/
Example 2:
Input:
(A*B)+(A*C)
Output:
AB*AC*+

logic:
*****
#A*(B+C)/D
#postfix- operators should be in increasing priority values
# pc > pl  - insert to output
# pc == Pl  - insert to output
# pc< pl    - insert into operators
#at end print all operators from last
'''
operator_dic = { '+' :1 , '-' :1,
                 '*' :2 , '/' :2,
                 '^' :3}
#init
i=0
finalop=[]              #final ouput stack
oprtrlst=[]             #Interim operator stack

ip=input()              #Input INFIX expression
l=len(ip)

for i in range(int(l)):
    if ip[i].isalpha():                 #append alphabets as  recieved
        finalop.append(ip[i])
    else:                               #operator loop
        if len(oprtrlst) ==0:           # append first operator in the expression to operator stack
            oprtrlst.append(ip[i])
        elif ip[i]== '(':               #insert open bracket as received
            oprtrlst.append(ip[i])
        elif ip[i]== ')':               #In case of close brackets - pop all the operator and append it to final op till relevent '( open bracket'
            notopen = True
            while notopen:
                if oprtrlst[-1] == '(':
                    oprtrlst.pop()
                    notopen=False
                else:
                    finalop.append(oprtrlst[-1])
                    oprtrlst.pop()
        else:                                               #Any other operator
            notdone= True
            while notdone:
                if len(oprtrlst)==0:                        #if operator stack is empty append the current operator
                    oprtrlst.append(ip[i])
                    notdone = False
                else:
                    op=oprtrlst[-1]                         #Take the Last operator in the operator stack
                    if op == '(' :                          #if its '(' append the che current operator without cheking precedence
                        oprtrlst.append(ip[i])
                        notdone = False
                    else:
                        pl=operator_dic[op]                 # pl = Priority of last operator in operator stack
                        pc=operator_dic[ip[i]]              # pc =priority of current operator from ip
                        if   pl > pc:                       #if pl is greater than pc append it to output stack
                            finalop.append(op)
                            oprtrlst.pop()
                        elif pc == pl:                      #if pl is equal to pc append to output stack
                            finalop.append(op)
                            oprtrlst.pop()
                        else:
                            oprtrlst.append(ip[i])          #if pc > pl  update operator stack
                            notdone = False


for i in range (len(oprtrlst)):                             #At end append the operators in stack - LIFO
        opr=oprtrlst[-1]
        finalop.append(opr)

for i in range (len(finalop)):                              #print output - POSTFIX expression
        print(finalop[i],end='')

