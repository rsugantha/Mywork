'''Fitness Checker Grade 15
The simple measure of body fitness is the BMI or Body Mass index. It depends only on the height L and weight W of a person.
 It is defined as BMI = [weight / height^2] where weight is taken in kilograms and height in meters.
Four general grades are proposed:
Underweight[U] – when BMI < 18.5
Normal weight[N] - 18.5 <= BMI < 25.0
Heavyweight [H] - 25.0 <= BMI < 30.0
Overweight [O] - 30.0 <= BMI
Write a program that takes in the Weight (in Kg) and Length (in meters) of an individual and displays the grade as U, N, H, O
Input :
The test case contains 2 space separated numbers W, L denoting the Weight and the Length. [W is an integer . H is a number with 2 decimal spaces]
Output
For the Test Case specify the BMI Grade as U,N,H or O
Example
Input
200 1.73
Ouput
O
Constraints :Consider all possible scenarios of exceptions that may occur while reading the weight and height
4.'''

WH = input("Enter the weight in KG and Enter the Height in meters: ").split()

#check if weight is an integer
try:
    W = int(WH[0])
except ValueError: print('Weight should be an Integer value')

try:
    W = WH[0]
    H = WH[1]
    if len(H[H.rfind('.') + 1:]) != 2:              #check if Height is a float with 2 decimal points
        raise Exception('Height Must have two numbers after decimal point')

    BMI = int(W) / float(H)**2                      #Calculate BMI
    print('BMI: ',BMI)

except IndexError:        print('Height is not received')  #When only one input is received
except ZeroDivisionError: print('Height cant be zero')     #when height is 0.00
except ValueError:        print('Weight should be integer and Height should be float')    #invalid entry
except KeyboardInterrupt: print('User quit')

#Print BMI in case of no exception
else:
    if    BMI < 18.5: print('Underweight[U]')
    elif  BMI >= 18.5 and BMI < 25.0: print('Normal weight[N]')
    elif  BMI >= 25.0 and BMI < 30.0: print('Heavyweight[H]')
    elif  BMI >= 30.0: print('Overweight[O]')


