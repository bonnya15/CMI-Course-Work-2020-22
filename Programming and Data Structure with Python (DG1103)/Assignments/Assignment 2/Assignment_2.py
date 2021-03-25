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

print(matched("zb%78"))
print(matched("(7)(a)"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
print(matched("(09998uish"))



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
        
print(listdiff([1,3,5],[1,2,4,6]))
print(listdiff([2,5],[2,5]))
print(listdiff([0,2,4,6],[1,3,5,7]))


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

p1 = {3:4, 0:3}
p2 = {3:-4,1:2}
addpoly(p1,p2)
addpoly({1:2}, {1:-2})

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
multpoly({1:2,0:1} , {1:2,0:-1})
multpoly({1:1,0:-1},{2:1,1:1,0:1})

