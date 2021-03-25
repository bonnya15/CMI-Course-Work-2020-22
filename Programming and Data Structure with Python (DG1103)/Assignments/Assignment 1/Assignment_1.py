# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:58:01 2021

@author: DELL
"""
import math

def sumofsquares1(n):
    s = []
    for i in range(1,int(math.sqrt(n))+1):
        s.append(i**2)
        if n-(i**2) in s:
          return(True)
    return(False)
    
print(sumofsquares1(2))
print(sumofsquares1(11))
print(sumofsquares1(3218))
print(sumofsquares1(3219))
    

def shuffle(l1 , l2):
    newlist  = []
    t = min(len(l1),len(l2))
    for x in range(t):
        newlist.append(l1[x])
        newlist.append(l2[x])
    if len(l1) > len(l2):
        for m in range(t , len(l1)):
            newlist.append(l1[m])
        return(newlist)
    else:
        for n in range(t, len(l2)):
            newlist.append(l2[n])
        return(newlist)
print(shuffle([0,2,4],[1,3,5]))  
print(shuffle([0,2,4],[1]))  
print(shuffle([0],[1,3,5]))
    

def removeduplicates(l3):
    nlist = []
    for k in l3:
        if k not in nlist:
            nlist.append(k)
        
    return(nlist)            
                
print(removeduplicates([7,2,5,7,2,9]))
print(removeduplicates([7,2,"hello",2,[5,5],"hello",9,[5,5]]))   

def splitwith(l4,p):
    plist = []
    index = [i for i in range(len(l4)) if l4[i] == p]
    j = 0
    for n in range(len(index)):
        plist.append(l4[j:index[n]])
        j = index[n]+1
    plist.append(l4[j:len(l4)])
        
    return(plist)
print(splitwith([7,2,5,7,[2,7],9],7)) 
print(splitwith([7,2,5,7,[2,7],9],8))  
print(splitwith([7,2,[8],8,[8],[[8],7],2,9],[8]))
print(splitwith([1,2,1],1))         

# another logic to  implement splitwith 
def splitwith1(l4 , p):
    l4.append(p)
    l = []
    k = []
    for i in range(len(l4)):
        if l4[i] == p:
             l.append(k)
             k = []
        else:
            k.append(l4[i])
    return(l)
            
                           
                   
        
    