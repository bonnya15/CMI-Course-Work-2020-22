# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:45:05 2021

@author: shiuli Subhra Ghosh, MDS202035
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def matched(s):
    left = []
    right = []
    for i in range(len(s)):
        if s[i] == '(':
            left.append(i)
        elif s[i] == ')':
            right.append(i)
    if len(left) != 0 and len(right) != 0  :
        return(len(left)==len(right))
    else: 
        return(False)


def listdiff(l1,l2):
    l = []
    for i in l1:
        if i not in l2:
            l.append(i)
    for j in l2:
        if j not in l1:
            l.append(j)
    l.sort()       
    return(l)
        



def addpoly(p1,p2):
    l1 = []
    l2 = []
    empty_dict = dict()
    for keys in p1.keys():
        l1.append(keys)
    for k in p2.keys():
        l2. append(k)
    for l in l1:
        if l in l2 and p1[l] + p2[l] !=0:
            empty_dict[l] = p1[l] + p2[l]
        elif l not in l2:
            empty_dict[l] = p1[l]
    for k in l2:
        if k not in l1:
            empty_dict[k] = p2[k]
    return(empty_dict)



def multpoly(p1,p2):
    l1 = []
    l2 = []
    empty_dict = dict()
    for keys in p1.keys():
        l1.append(keys)
    for k in p2.keys():
        l2. append(k)
    for i in range (len(l1)):
        for j in range (len(l2)):
            empty_dict = addpoly(empty_dict,{i+j : (p1[i]*p2[j])})
    return(empty_dict)


