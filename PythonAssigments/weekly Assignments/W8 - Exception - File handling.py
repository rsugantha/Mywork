'''Perform following file Operations Grade 15
1.Create/open a file and write some text data into the file
2.Read its content
3. Go to the specified location
Ask user whether the operation to be continued after completion of one operation . Continue file operations till user
do not want to perform any further operations.
Constraints : Think about all possible scenarios where exception could occur and apply exception handling to protect system from crashing
Assumption
File is not created
Input
Enter one of the options mentioned above
Output
Print error in case exception occurs otherwise print “Operation performed Successfully”
Input
Enter the option : 2
Output
Oops! File does not exist
Input
1
Enter file name : file1.txt
Output
file1.txt is created
Operation performed Successfully
Input
3
Enter the position -2 0 # Seek from beginning with seek position entered negative
Output
Seek position can not be negative'''

#user defined errors
class Error(Exception): #"""Base class for other exceptions"""
    pass
class SeekNoError(Error):
    pass
class OpcheckError(Error):
    pass
#Eo user defined errors
#
#fn - open and write data to given file
def openwrit(fn):
    f = open(fn,'w')
    f.write('Hello All\nfirst line\nsecond line \nCode is like humor. When you have to explain it, it’s bad.')     #write contents to New file
    print(fn, 'is Created')
    f.close()

#fn -Read given file and print its contents
def readfile(fn):
    fr = open(fn,'r')
    contents = fr.read()
    print(contents)

#fn-Seek the given position in the given file
def gotoloc(fn,l,wh):
        if  l < 0:
            raise SeekNoError
                #Exception("Seek position can not be negative")
        else:
            fl = open(fn, 'r')
            fl.seek(l,wh)
            print('Current position:',fl.tell())                #print the current position
            cl = fl.read()                                      #Read the current line
            if cl == '': raise EOFError                         #Raise eof if the read is empty
            else: print(cl)

            fl.close()

#fn- to check whether user wants to continue
def quitorgo():
    Notquit = True
    print(''' ********************************************
Please select one of the below option\n1.Continue doing other operations \n2.Quit''')
    uin = input('Continue the operation? or Quit?: ')

    if int(uin) == 1:                   #User wants to continue
        Notquit = True
    elif int(uin) == 2:                 #user wants to quit
        print('Bye bye!')
        Notquit = False
    else:
        print('Bad input..Tryagain')    #Bad input
        quitorgo()
    return Notquit

#main
Notquit = True
while Notquit:

    print('''**********************************************************\n
1.Create/open a file and write some text data into the file
2.Read its content
3. Go to the specified location''')

    try:
            inp = input('Enter one of the options mentioned above: ')
            op = int(inp)
            fn = input('Enter file name : ')
            if   op == 1:  openwrit(fn)
            elif op == 2:  readfile(fn)
            elif op == 3:
                lwh = input('Enter the position: ').split()
                l = lwh[0]
                wh = lwh[1]
                gotoloc(fn,int(l),int(wh))
            else:
                raise OpcheckError

    except OpcheckError: print("Enter valid operation to perform")
    except SeekNoError: print('Seek value cant be negative!!')
    except FileNotFoundError: print('Oops! File does not exist..Create file before other operations')
    except ValueError: print('Enter valid number')
    except IndexError: print('Enter Two arguments')
    except TypeError:  print('Validate the inputs')
    except EOFError:   print('Eof reached')
    except IOError:    print('Provide valid seek positions')

    else:
        print('\nOperation performed Successfully\n')

    Notquit = quitorgo()