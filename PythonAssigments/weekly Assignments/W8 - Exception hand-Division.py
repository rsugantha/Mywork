'''Division in python Grade : 10
Write a program to calculate the difference between division and floor division of two float values
Input
Two float values a and b >
Output
Difference between division and floor division when a is divided by b
Example 1
Input
5.0 2.0
Output
0.5
Explanation
5.0 divided by 2.0 = 2.5
5.0 divided 2.0 and floored is = 2.0
2.5 - 2.0 = 0.5
Example 2
Input
15.0 4.0
Output
0.75
Constraints : Apply exception for divide by zero error'''


inp=input("Enter the numbers: ").split()        #Input
try:
    a = float(inp[0])
    b = float(inp[1])
    d = a / b           # Division
    df = a // b         # Floored division
    print(d,df)
except ZeroDivisionError:                       #Handle divide by zero error
    print('Divide by zero error')
except ValueError:
    print('Input is not Integer or Float')      #Handle inavlid input error
else:                                           #Calulate and print output
    out = d - df
    print("output: ",out)
