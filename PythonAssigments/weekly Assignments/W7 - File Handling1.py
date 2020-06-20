'''
Perform following file Operations Grade 10
1 Create a new file “python_applications.txt” and write the following list in it
• Science
• System Administration
• Web Development
• Application Development
• Developing Games
• Artificial Intelligence
2.Read the newly created file and print its content
3. Go to the end of the file and append one more entry as given below and print the file contents
• Testing Scripts
'''
#open a file in write mode
new_file=open('python_applications.txt','w')
#write contents to New file
new_file.write('• Science\n• System Administration\n• Web Development\n• Application Development\n• Developing Games\n• Artificial Intelligence')
new_file.close()
#
#
#Read the New file to variable and print it
new_file=open('python_applications.txt','r')
nc = new_file.read()
print("The contents of the file are below:\n",nc)
new_file.close()
#
#
#Append New entry
new_file=open('python_applications.txt','a')
new_file.write('\n• Testing Scripts')
#
#Check if the value is appended
new_file=open('python_applications.txt','r')
na = new_file.read().split('\n')
if na[-1]=='• Testing Scripts':
    print("\n\nValue appended Successfully")
new_file.close()

#import os
#print(os.getcwd())