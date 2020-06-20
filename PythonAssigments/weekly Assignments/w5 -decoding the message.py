'''
4. Alan Turing
Alan Turing and his team intercept a message. They receive an encrypted String.
To Help their country win the World War they need to Decrypt the String . The
Team is able to observe a pattern in the Encryption. The pattern in which the
strings were encypted is as follows
Encypted Text : 3[b2[ca]]
Original Text: bcacabcacabcaca
Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. Each test case contains a string s.
Output:
For each test case in a new line print the required decoded string.
Constraints:
1<=T<=10
1<=length of the string <=30
Example 1:
Input:
2
1[b]
3[b2[ca]]
Output:
b
bcacabcacabcaca
Example 2:
Input:
2
1[a]
2[ba]
Output:
a
baba
'''

#inputs
T=input('Enter the no of Test cases:')
inpt=[]
for i in range(int(T)):                             #receive inputs and append to input stack
    x=input('Enter the encoded string:')
    inpt.append(x)

#create outputs for testcases one by one
for i in range(int(T)):
    ip = inpt[i]
    l=len(ip)
    out=[]

    def calcexp():                                  #calculate expression
        exp = []
        while out[-1] != '[':
            exp.insert(0,out[-1])
            out.pop(-1)
        out.pop()
        exp = ''.join(map(str, exp))
        return exp
    #eof

    for i in range(int(l)):
        op = ip[i]
        if op == ']':                        #on reaching close bracket calculate the values inside the brackets
            exp = calcexp()
            n = int(out.pop(-1))             #number before the open braces
            oexp = lambda n , exp : n * exp  #repeating the expression by n
            out.append(oexp(n,exp))
        else:                                #in case of '[' and alphabets insert into stack as it is
            out.append(op)

    out = ''.join(map(str, out))             #convert list to string
    outmsg='The decoded message for string {} is : {}'
    print(outmsg.format(ip,out))             #print the output