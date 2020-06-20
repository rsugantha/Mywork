'''Count the number of occurences of a word in a file'''

#Get user input - word
w = input('Enter the word:')
w = w.lower()                     #change the user input to lower case -  To ignore type mismatch
print(w)

#Open the file in Read
tf = open('Pythontext.txt','r+')
ta = tf.read().split()            #Read the file into array

count=0                           #word counter
for x in ta:
    xa = x.lower()                #change the file input to lower case -  To ignore type mismatch
    if xa == w:
        count += 1

print('The word',w,'has occured',count,'times')

tf.close()                        #File close
