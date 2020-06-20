'''Write a program that appends one file to another
Note : Use python_applications.txt file and append sample.txt (modified) at the end of it'''

file2=open('Sample.txt','r')
nc = file2.read()
print("The contents of the file are below:\n",nc)
file2.close()
#
#Append file2 contents to file1
file1=open('python_applications.txt','a')
file1.write('\n')
file1.write(nc)