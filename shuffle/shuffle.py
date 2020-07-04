import random
import enchant
import math
n=input("enter::")
x=0
def sp(n):
    n=n.split(" ")
    l=len(n)
    for i in range(0,l):
        p=n[i]
        d=lis(p)
        che(d)
        continue
def che(s):
    z=enchant.Dict("en-US")
    y=z.check(s)
    if y is False:
        x=0
        s=list(s)
        shuf(s)
    else:
        x=1
        print(s)
        return 
def lis(n):
    str1 = ""    
    for ele in n:  
        str1 += ele
    return str1
def shuf(s):
    if x!=1:
        random.shuffle(s)
        d=lis(s)
        che(d)
        s=list(d)
    return
if __name__=="__main__":
    sp(n)
