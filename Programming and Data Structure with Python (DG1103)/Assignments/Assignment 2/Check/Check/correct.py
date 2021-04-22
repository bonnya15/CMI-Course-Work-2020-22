###########

def matched(s):
    nesting = 0
    for c in s:
        if c == '(':
            nesting = nesting + 1
        elif c == ')':
            nesting = nesting - 1
        if nesting < 0:
            return(False)
    return(nesting == 0)

###########

def listdiff(l1,l2):
    (m,n) = (len(l1),len(l2))

    (i,j,ldiff) = (0,0,[])

    while (i+j < m+n):
        if i == m:
             ldiff.extend(l2[j:])
             j = n
        elif j == n:
             ldiff.extend(l1[i:])
             i = m
        elif l1[i] == l2[j]:
             (i,j) = (i+1,j+1)
        elif l1[i] < l2[j]:
             ldiff.append(l1[i])
             i = i+1
        elif l2[j] < l1[i]:
             ldiff.append(l2[j])
             j = j+1

    return(ldiff)

###########

def cleanup(p):
    newp = {}
    for exp in p.keys():
        if p[exp] != 0:
            newp[exp] = p[exp]
    return(newp)


def addpoly(p1,p2):
    presult = p1
    for exp in p2.keys():
        try:
            presult[exp] = presult[exp] + p2[exp]
        except KeyError:
            presult[exp] = p2[exp]
    return(cleanup(presult))
                
def multpoly(p1,p2):
    presult = {}
    for exp1 in p1.keys():
        for exp2 in p2.keys():
            exp = exp1+exp2
            try:
                presult[exp] = presult[exp] + p1[exp1]*p2[exp2]
            except KeyError:
                presult[exp] = p1[exp1]*p2[exp2]
    return(cleanup(presult))
                
                
                
