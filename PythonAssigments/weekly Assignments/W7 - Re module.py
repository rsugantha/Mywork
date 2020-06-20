'''
Pattern matching using re module Grade : 15
Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores using re(Regular Expression)
Input:
Input consists of a string
Output:
Prints “Found a match” if the string contains uppercase or lowercase alphabets or numbers or underscore. Otherwise prints “Not matched”
Example:
Input:
Python_Exercises_1
Output:Found a match
Input:
The quick brown fox jumps over the lazy dog
Output:
Not matched

'''

#Import Regular Expression module
import re

txt = input('Enter the string: ')

x = re.search("[a-zA-Z]", txt)               #Check if the string has Upper and Lower case alphabets
if x:                                        #If true - Check for numbers
    x = re.search("[0-9]", txt)
    if x:                                    #If true - Check for Underscore
        x = re.search("[_]", txt)
        if x: print('Found a match')         #Print 'Matched' only when all conditions are true
        else: print('Not matched')
    else: print('Not matched')
else : print('Not matched')