#print(26+26)
'''
#dictionaries

child1={
    "name": 'Rishav',
    "year": 2017
}
child2={
    "name":'Rishav1',
    "year": 2018
}

myfamily={
    "child1":child1,
    "child2":child2
}
for x in myfamily.values():
'''
#x=myfamily["child2"]
#    print(x)
#Tuple are unchangeable

#thistuple=('apple',)   #tuple with only one element needs a comma, otherwise its just a string
#print(type(thistuple))


"""
#lists
lista = ['apple','orange','grapes']
for x in lista:
    print(x)

listb=[]
listb.append('hi how are you')
listb.insert(0,'hello')
listb.pop()
listb.clear()
listc=lista.copy()
listd=lista+listc

listaa=[1,2,3]
listbb=['a','b','c']
for x in listaa:
    listbb.append(x)
print(listbb)

listbb.extend(lista)
print(listbb)

listbb.reverse()
print(listbb)

for x in range(3,5):
    listbb.pop(x)
listbb.remove(2)
print(listbb)
listbb.sort()
print(listbb)

#del listb
"""
"""
print("hello world")
x = input('enter num',)
if int(x) > 2:
    print('x is big')
else:
    print(2)

#variable declaration
x,y,z = 11,2,'orange'
a = b = ab = 'rishav'
if x>y:
 print(x)
print(z+' is sweet')  #adding comments to variable

print(a,b,ab)

#global variable
x ='one'
z= 3
def myfun():
    x ='localone'
    global y    #global variables can be declared as well as changed inside a function
    y ='two'
    global z
    z = 5
    print('local= '+ x)

myfun()
print('global ='+ x)
print(y)
print(z)

#Data type can be changed from one type to another but complex cannot be changed
x = 5.2
print(int(x))

print(type(x))  #to know the type of var

#to create random numbers
import random
print(random.randrange(1,5))
'''
# strings
a='Rishav'
print(a[1])  #strings are arrays starting with 0=index
print(a[0:6]) #slicing string ; a[startpos:no of char]
print(a[-6:-4]) # negative indx;start slicing from back ; a[-startpos from back:-no of char]
print(len(a))   #len of str
print(a.upper())    #convert to upper or lower case
'''
b='   rishav,my son '
print('b=',b)
print('striped b=',b.strip())  #strip removed white spaces in start and end

print(b.replace("s",'S'))   #replaces all mentioned alphabets

print(b.split('a'))     #splits the string by given character

x= 'my' in b            #in and not in to check for string in text
print(x)

#format - used to pass arguments - combine str +number
x=10
y=4
z=5
str='x is {2},y is {0},z is {1}'    #manual numbering - note change in ip order
print(str.format(y,z,x))
str1='x is {},y is {},z is {}'    # automatic
print(str1.format(x,y,z))

#escape characters
a="go \b corona \t go \ngo"
b='\x48'  #hex
c="110"     #oct
print(b,c)

#encode function
txt = "My name is Ståle"    # default UTF-8
x = txt.encode()
print(x)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(txt.encode(encoding="ascii",errors="strict"))

#reversing string
a="hello"
print(a[::-1])


'''
#lambda function:
'''
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(4))'''