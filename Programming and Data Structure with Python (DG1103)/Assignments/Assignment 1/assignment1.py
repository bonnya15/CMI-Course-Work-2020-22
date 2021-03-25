# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:58:01 2021

@author: Shiuli 
"""
import math

def sumofsquares(n):
    s = []
    for i in range(1,int(math.sqrt(n))+1):
        s.append(i**2)
        if n-(i**2) in s:
          return(True)
    return(False)
    

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
 

def removeduplicates(l3):
    nlist = []
    for k in l3:
        if k not in nlist:
            nlist.append(k)
        
    return(nlist)            
 
            

def splitwith(l4,p):
    plist = []
    index = []
    for i in range(len(l4)):
        if p == l4[i]:
           index.append(i)
    j = 0
    for n in range(len(index)):
        plist.append(l4[j:index[n]])
        j = index[n]+1
    plist.append(l4[j:len(l4)])
        
    return(plist)
      

            
                           
                   
        
    