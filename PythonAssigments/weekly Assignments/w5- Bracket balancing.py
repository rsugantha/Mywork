'''3. Bracket Balancing
There are three types of matched pairs of brackets: [], {}, and ().
A matching pair of brackets is not balanced if the set of brackets it encloses
are not matched. For example, {[(])}is not balanced because pair of square
brackets encloses a single, unbalanced opening bracket, (, and the pair of
parentheses encloses a single, unbalanced closing square bracket, ].
By this logic, we say a sequence of brackets is considered to be balanced if
the following conditions are met:
* It contains no unmatched brackets.
* The subset of brackets enclosed within the confines of a matched pair of
brackets is also a matched pair of brackets.
Given strings of brackets, determine whether each sequence of brackets is
balanced. If a string is balanced, print YES on a new line; otherwise,
print NO on a new line.
Input Format
Testcase consists of a single string, denoting a sequence of brackets.No spaces
between the terms
Output Format
For each string, print whether or not the string of brackets is balanced on a
new line. If the brackets are balanced, print YES; otherwise, print NO.
Example 1:
Input
({(){}[]})[]
Output
YES
Example 2:
Input
({())
Output
NO'''


ip=input()                                   #recieve ip exp without spaces
l=len(ip)

oplst=[]                                    #empty op stack
balanced = True

if int(l) % 2 == 0:                          #check whether the input has even number of brackets  -else print its unbalanced directly
    for i in range (int(l)):
            if ip[i] == '(' or ip[i] == '[' or ip[i] == '{':        #add the open brackest to stack
                oplst.append(ip[i])
            elif ip[i] == ')':                                      #on receiving close brackets check whther relevent open bracket is present
                if oplst[-1] == '(':
                    oplst.pop()                                     #match present - pop it out of stack
                else:
                    balanced = False                                #match not present - end the loop
            elif ip[i] == ']':
                if oplst[-1] == '[':
                    oplst.pop()
                else:
                    balanced = False
            elif ip[i] == '}':
                if oplst[-1] == '{':
                    oplst.pop()
                else:
                    balanced = False

else: balanced = False                                              #odd number of brackets - End the loop

#check if balanced and all operators in stack has been cleared and print the message

if balanced and len(oplst) == 0:    print("Yes - The expression is balanced")
else:                               print("NO - The expression is not balanced")