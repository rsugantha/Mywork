'''Count total number of words in a given file'''

#open a file in read mode
f = open('sample.txt','r')
nw = f.read().split()
n = len(nw)                                         #length of array = count
print("The number of words in the file is: ",n)
f.close()
