N=7
a=(1,2,3,3,3,2,1)
i=0
pf=''  #Previous flag
op=''  #Final output
while(i<N-1):
   if a[i]<a[i+1] and pf=='':
       pf='In'
       op='Yes'
   else:
       if a[i]==a[i+1] and pf=='In':
            pf='Eq'
            op='Yes'
       elif a[i] >a[i+1] and pf=='Eq':
           op ='Yes'
       else:
           op='No'
   i+=1
if op=='Yes': print('Bellcurve')
else:print('Not bellcurve')

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end = '')



