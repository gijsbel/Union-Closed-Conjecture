from itertools import chain, combinations
from random import sample
import math

def familyFromList(L):
    return set(frozenset(i) for i in L)

# pretty prints a family
def printFamily(family):
    print([list(m) for m in family])

# checks if a family is union closed
def isUnionClosed(family):
    for m in family:
        for n in family:
            if m.union(n) not in family:
                #print("The union of "+str(list(m))+" and "+str(list(n))+" is not in the family")
                return False
    return True

# make a family union-closed
def makeUnionClosed(family):
    c = family.copy()
    for m in family:
        for n in family:
            c.add(m.union(n))
    return c

# finds how many members of the family contain a certain element
def numberOfAppearances(family, element):
    n = 0
    for m in family:
        if element in m:
            n += 1
    return n

# returns the set that contains all relevant elements of the family
def getGroundPlane(family):
    a = set()
    for m in family:
        a = a.union(m)
    return a

# finds the most common elements in the family
def mostCommon(family):
    a = getGroundPlane(family);
    m = set()
    n = 0
    for e in a:
        k = numberOfAppearances(family,e)
        #print(str(e)+" appears "+str(k)+" times")
        if k==n:
            m.add(e)
        if k>n:
            n = k
            m = set()
            m.add(e)
    return m

# checks if the most apparant element is in at least
# half of the members of the members of the family
def hasCommon(family):
    e = mostCommon(family)
    if(len(e)==0):
        return False
    return numberOfAppearances(family,e.pop())>=len(family)/2


# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
def powerset(aset):
    s = list(aset)
    p = set()
    for r in range(len(s)+1):
        p = p.union(set(frozenset(i) for i in combinations(s, r)))
    return p

# finds the minimal members
# that is, the members that do contain properly contain another member
# except for the empty set
def minimalMembers(family):
    minimalset = set()
    for m in family:
        minimal = True
        for n in family:
            if len(n)>0 and (not n is m):
                if n.issubset(m):
                    minimal = False
                    break
        if minimal:
            minimalset.add(m)
    return minimalset

# union of the minimal members
def minimalElements(family):
    minElements = set()
    minMembers = minimalMembers(family)
    for m in minMembers:
        for e in m:
            minElements.add(e)
    return minElements

#chooses k random subsets from the set {1, ..., n}
#every subset has the same probability of being chosen
def randomFamily(n,k):
    P = powerset(range(1,n+1))
    return set(sample(P,k))

"""
F = [[1,2],[1],[3],[4,3],[4]]
F = familyFromList(F)
F = randomFamily(4,6)

printFamily(F)
print("union closed: ",isUnionClosed(F))
print("ground plane: ",getGroundPlane(F))
print("most apparant:",mostApparant(F),numberOfAppearances(F,mostApparant(F)))
print("common:",hasCommon(F))

F = makeUnionClosed(F)
printFamily(F)
print("union closed: ",isUnionClosed(F))
print("ground plane: ",getGroundPlane(F))
print("most apparant:",mostApparant(F),numberOfAppearances(F,mostApparant(F)))
print("common:",hasCommon(F))
"""

"""
n = 7
P = powerset(range(1,n+1))
for k in range(1,2**n+1):
    print(k)
    c = 0
    for i in range(10000):
        f = set(sample(P,k))
        if hasCommon(f):
            c += 1
        #else:
            #printFamily(f)
    print(c/10000)
"""

n = 4
P = powerset(powerset(range(1,n+1)))
c = 0
print("Their are ",len(P)," families in total")
for f in P:
    #skip empty
    if len(f)==0:
        continue
    
    minElements = minimalElements(f)
    mostApp     = mostCommon(f)
    hasCom      = hasCommon(f)
    unionClos   = isUnionClosed(f)

    if unionClos:
        #if not mostApp.issubset(minElements):
            #printFamily(f)
            #print(minElements)
            #print(mostApp)
            #print("SUPER WTF")
        if len(mostApp.intersection(minElements))==0:
            printFamily(f)
            #print(minElements)
            #print(mostApp)
            print("SUPER WTF")
    if hasCom:
        c += 1
        if not unionClos:
            printFamily(f)
            print(mostApp)
    else:
        if unionClos:
            print("THIS IS VERY WRONG")
print(c/(2**(2**n)))

    
