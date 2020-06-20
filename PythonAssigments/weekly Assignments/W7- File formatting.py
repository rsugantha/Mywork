'''Formatting a file Grade 15
Given a text file containing one paragraph. One has to insert a newline character (\n) at the end of every sentence
and rewrite the modified text in another file . Verify the formatting done by printing the contents of the newly created file'''

#Open the file in Read
tf = open('Pythontext.txt','r+')
ta = tf.read().split('.')       #Read the file into array
#print(ta)
tf.close()

#Modify the contents Write it to new file
ntf = open('Pythonnewtext.txt','w')      #new text file
mt=''
for x in ta:
    mt = x + '.' + '\n'                  #Add new line character
    ntf.write(mt)
ntf.close()

#Read and display the modified file
ntf = open('Pythonnewtext.txt','r')
ta = ntf.read()
print(ta)
ntf.close()