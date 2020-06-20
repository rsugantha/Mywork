#import operator as op
sdict = {}

def updict(name,score): # using __setitem__ method
    sdict.__setitem__(name,score)
    return sdict
for i in range(int(input())):
    name = input()
    score = float(input())
    sdict=updict(name,score)

print(sdict)
#sortd=sorted(sdict.items(),key=op.itemgetter(1))
sortd=sorted(sdict.items(),key=lambda x:x[1])
print(sortd)

#runner=sortd[1]
rscore=sortd[1][1]
print(rscore)