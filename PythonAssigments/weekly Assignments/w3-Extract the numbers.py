'''3. Extract The Number
Bharat is given a string that contains text and numbers.
Bharat needs to extract the number from the string such that the number must not contain the integer 9.
NOTE: In case there any multiple numbers that match the condition, Print all numbers in a space separated format( in same order that they appear in the string)
For eg if the string contains "My pin code is 560047 and phone number is 98998" ,
Bharth only needs to extract 560047 and not 98998.
You need to help him extract the number.
Input:
The testcase consists of a String
Output:
Output the extracted number.
Example:
Sample Input 1:
This is alpha 5057 and 97
Sample Output 1:
5057
Sample Input 2:
I have 2 numbers 400 and 380
Sample Output 2:
2 400 380
'''
#inputs
str=input('Enter the string:').split()

for i in range(len(str)):
    if(str[i].isnumeric()):                #check if the array element is numeric
        if(str[i].rfind("9") < 0):         #Check if '9' is present
            print(str[i],end=' ')          #prints the num if 9 is not present