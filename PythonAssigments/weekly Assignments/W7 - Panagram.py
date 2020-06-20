'''Panagram string using string module Grade : 15
Given a String print if the string is a pangram or not
A pangram is a word or a sentence that has all the letters of the English alphabet in it.
Input
Input consists of a string.
Output:
Output print "Pangram" if the string is a pangram, or else print "Not Pangram".
Example 1:
The quick brown fox jumps over the lazy dog
Output
Pangram
Example 2:
Input
She sells on the sea shore
Output
Not Pangram'''

#Import Regular Expression module
import re

txt = input('Enter the string: ')

txt = txt.lower()
x = re.findall("[a-zA-Z]", txt)               #Check if the string has Upper and Lower case alphabets
if x:                                         #If true
    x_set = set(x)                            #Create a unique set of alphabets
    l = len(x_set)
    if l == 26:                              #If length of unique set is 26 - IT means all alphabets are present in given string
        print('Pangram')
        print('The given string has all 26 english alphabets')
    else:
        print('Not Pangram')
        print('The given string has only below',l ,'english alphabets')
        print(x_set)