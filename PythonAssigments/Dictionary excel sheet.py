exceldictn ={
    'A' : 1, 'B': 2,'C' : 3, 'D': 4,'E' : 5, 'F': 6,'G' : 7, 'H': 8,'I' : 9, 'J': 10,'K' : 11, 'L': 12,'M' : 13, 'N': 14,
'O' : 15, 'P': 16,'Q': 17, 'R': 18,'S' : 19, 'T': 20,'U' : 21, 'V': 22,'W' :23, 'X': 24,'Y' : 25, 'Z': 26
}
a=''
op=0
S=input()
col=S.upper()
sl=len(S)         #length of given ip
p=sl              #Power = length of ip
for i in range(sl):
    a=col[i]
    p=p-1          # keep reducing power as per position
    c=exceldictn[a]    #taking dictionary value
    b=26**(p) *c        #formula
    op=op+b
print(op)
