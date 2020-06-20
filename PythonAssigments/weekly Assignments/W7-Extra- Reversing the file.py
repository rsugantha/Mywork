'''Write a python program to reverse the content of a file and store it in another file'''

f = open('Sample.txt','r')

fc = f.read().split()
print(fc)
st = ' '.join(list(reversed(fc)))                       #reverse the list and make it a string
nf=open('reversedfile.txt','w')
nf.write(st)
nf.close()

f = open('Sample.txt','r')
r = f.read().split()
s=[]
for x in r:
    s.append(x[::-1])                                   #reverse the elements in list and make it a string
st = ' '.join(list(s))
nf=open('reversedbywordfile.txt','w')
nf.write(st)
nf.close()

f.close()                                               #Close the input file