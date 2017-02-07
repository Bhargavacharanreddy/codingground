from random import randrange, seed
from WalshHadamard import *
 
seed(2015)
 
X=[ 10,14,11,-6,5,4,4,-1,7,10,4,6,6,7,7,3 ]
 
print("X = ")
print(X)
print("Slow WHT(X) = ")
print(WHT(X)[0])

print("Fast WHT(X) = ")

print(FWHT(X))
sums=0
for i in FWHT(X):
    sums=sums+i
sums=sums/16


diff=0
for i in FWHT(X):
    diff=diff+((sums-i)*(sums-i))
    
diff=sqrt(diff/16)
print("ARithmatic Mean of these values is "+str(sums))
print("Standard Deviation of these values is "+str(diff))