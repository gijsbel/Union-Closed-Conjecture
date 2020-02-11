from itertools import chain, combinations
from random import sample
import math

def familyFromList(L):
    return set(frozenset(i) for i in L)

# pretty prints a family
def printFamily(family):
    print([list(m) for m in family])

def mixFamilies(family1, family2):
    newfam = set()
    for m in family1:
        for n in family2:
            newfam.add(m.union(n))
    return newfam

# checks if a family is union closed
def isUnionClosed(family, output=False):
    for m in family:
        for n in family:
            u = m.union(n)
            if u not in family:
                if output:
                    print("The union of "+str(list(m))+" and "+str(list(n))+"="+str(list(u)) +" is not in the family")
                return False
    return True

# checks if a family is intersection closed
def isIntersectionClosed(family, output=False):
    for m in family:
        for n in family:
            i = m.intersection(n)
            if i not in family:
                if output:
                    print("The intersection of "+str(list(m))+" and "+str(list(n))+"="+str(list(i))+" is not in the family")
                return False
    return True

# make a family union-closed
def makeUnionClosed(family):
    c = family.copy()
    for m in family:
        for n in family:
            c.add(m.union(n))
    return c

# make a family intersection-closed
def makeIntersectionClosed(family):
    c = family.copy()
    for m in family:
        for n in family:
            c.add(m.intersection(n))
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
def mostCommon(family, output=False):
    a = getGroundPlane(family);
    m = set()
    n = 0
    for e in a:
        k = numberOfAppearances(family,e)
        if output:
            print(str(e)+" appears "+str(k)+" times")
        if k==n:
            m.add(e)
        if k>n:
            n = k
            m = set()
            m.add(e)
    return m

# finds the least common elements in the family
def leastCommon(family, output=False):
    a = getGroundPlane(family);
    m = set()
    n = 10000000000
    for e in a:
        k = numberOfAppearances(family,e)
        if output:
            print(str(e)+" appears "+str(k)+" times")
        if k==n:
            m.add(e)
        if k<n:
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

# checks if the least apparant element is in at most
# half of the members of the members of the family
def hasRare(family):
    e = leastCommon(family)
    if(len(e)==0):
        return False
    return numberOfAppearances(family,e.pop())<=len(family)/2


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

# given an universe, returns the complement of the set
def complementSet(aset, universe):
    return universe.difference(aset)

# given a family, returns the complement family by
# taking the complement of every member
# if no universe is specified, it is assumed to be 
# the ground plane of the family
def complementFamily(family, universe=None):
    cfam = set()
    if not universe:
        #print("No universe given; using ground plane")
        universe = getGroundPlane(family)
    for m in family:
        cfam.add(frozenset(complementSet(m,universe)))
    return cfam

# given a family, returns the supercomplement
def superComplementFamily(family, universe=None):
    cfam = set()
    if not universe:
        #print("No universe given; using powerset of ground plane")
        universe = powerset(getGroundPlane(family))
    return universe.difference(family)

#chooses k random subsets from the set {1, ..., n}
#every subset has the same probability of being chosen
def randomFamily(n,k):
    P = powerset(range(1,n+1))
    return set(sample(P,k))


#
def inspectFamily(F):
    print("Family:")
    printFamily(F)
    print("Number of members:", len(F))
    print("Ground Plane:",getGroundPlane(F))
    print("Union Closed:", isUnionClosed(F, output=True))
    print("Intersection Closed:", isIntersectionClosed(F, output=True))
    print("Minimal Members:")
    printFamily(minimalMembers(F))
    print("Minimal Elements:", minimalElements(F))
    print("Most Common:", mostCommon(F, output=True))
    print("Least Common:", leastCommon(F))
    print("Has Common?:", hasCommon(F))
    print("Has Rare?:", hasRare(F))
