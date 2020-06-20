'''Oreo Biscuits
Given an array A[] of N integers where each value represents number of Oreo Biscuits in a packet.
Each packet can have variable number of Oreo Biscuits.
There are m students, the task is to distribute Oreo packets such that :
1.Each student gets one packet.
2.The difference between the number of Oreo Biscuits given to the students in packet with maximum Oreo Biscuits and packet
with minimum Oreo Biscuits is minimum.Try not to use in-built sort functions.
Input:
Each test case consists of three lines. The first line of each test case contains an integer N denoting the no of packets.
Then in the next line are N space separated values of the array A[] denoting the values of each packet.
The third line of each test case contains an integer m denoting the no of students.
Output:
For each test case in a new line print the required answer .
Example 1:
Input:
7
7 3 2 4 9 12 56
3
Output:
2
Explanation
Input : N = 7
A[] = {7, 3, 2, 4, 9, 12, 56}
m = 3
Output: Minimum difference is 2
We can pick 2, 3 and 4 and get the minimum difference between maximum and minimum packet
sizes. ie 4 - 2 = 2
Example 2:
Input:
6
2 3 8 4 7 12
2
Output:
1
Explanation
Input : N = 6
A[] = {2, 3, 8, 4, 7, 12}
m = 2
Output: Minimum difference is 1
We can pick 2, 3 and get the minimum difference between maximum and minimum packet
sizes. ie 3 - 2 = 1'''

#inputs
N = input('Enter the no of packets: ')
A = input("Enter the no of biscuits in the pockets: ").split()
m = input('Enter the no of Students: ')

def sortin(A):
    for i in range(int(N)):                 #sort the input array
        for j in range(int(N) - 1):
            if (int(A[i]) > int(A[j])):
                j += 1
            else:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    A = list(map(int,A))
    print('Sorted packets',A)

def combinations(A):                        #Create a sublist of possible combinations
    p = []
    for i in range(int(N)):
        for j in range(i,int(N)+1):
            comb =(A[i:j])
            comb=list(map(int, comb))
            if len(comb) == int(m):         # pick the possible combinations for m students
                p.append(comb)
    return p

def calmindiff(pc):                           #Calculate and append min diff value
    for i in range (len(pc)):
        mnp=pc[i]
        mn=mnp[int(m) -1] - mnp[0]
        pc[i].append(mn)
    print("combinations with thier diff value:",pc)
def sortbymindiff(pc):                      #sort the array by min diff value
    lp=len(pc[0])
    mdiffpos=lp-1
    l = int(len(pc))
    for i in range(l):
        for j in range(1,l-1):
            if int(pc[j][mdiffpos]) > int(pc[j+1][mdiffpos]):
                temp = pc[i]
                pc[i] = pc[j+1]
                pc[j+1] = temp

    mdiff = pc[0][mdiffpos]                 # minimum diff value
    out=[]
    for i in range(int(len(pc) -1)):        #Pick the combinatons with same min diff value
        xx=pc[i][mdiffpos]
        if xx == mdiff:
           pc[i].pop()
           out.append(pc[i])

    return mdiff , out
'''
    o = dict()
    o['Minimum diff value possible is: '] = mdiff
    o['Packet Combinations with min diff value :'] = out
    return o
'''

#Main loop
sortin(A)                                #Sort the input array
pc = combinations(A)                     #create possible combinations for given students
print('Possible combinations: ',pc)
calmindiff(pc)                           #append mininmun difffernece value to every possible combinations
mdiff,o = sortbymindiff(pc)              #Sort by min diff value and pick the combinations with the same min difference

print('Minimum diff value possible is: ',mdiff)
print('Packet Combinations with min diff value are ',o)