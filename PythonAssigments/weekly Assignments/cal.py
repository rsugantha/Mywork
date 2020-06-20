#Calculation Module
# Recieves the below inputs tp calc function
# n = Number inputs
# op = Operator
# l  = length of n(input)

def addtn(n):                   #Addtion
    sumn = 0
    for x in n:
        sumn +=x
    return sumn

def sub(n,l):                   #Subtraction
    d = n[0]
    for i in range(1 , l):
        d = d - n[i]
    return d

def mul(n,l):                   #Multiplication
    m = n[0]
    for i in range(1 , l):
        m = m * n[i]
    return m

def divtn(n,l):                #Division
    dv = n[0]
    for i in range(1 , l):
        if n[i] != 0:
            dv = dv / n[i]
        else:
            dv = 'Divide by zero error'
    return dv

def calc(n, op, l):             # Call fn based on operator
    if   op == 1: return addtn(n)
    elif op == 2: return sub(n,l)
    elif op == 3: return mul(n, l)
    elif op == 4: return divtn(n, l)


