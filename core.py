from itertools import chain, combinations
from random import sample
from operator import xor
import math
import warnings

def familyFromList(L):
    return set(frozenset(i) for i in L)

# cardinality of the family
def membersAmount(family):
    return len(family)

# sum of the cardinality of the members
def cumulativeMemberSize(family):
    s = 0
    for m in family:
        s += len(m)
    return s

# calculates the average occurence of an element, does a smart
# double counting argument
def averageOccurence(family):
    gps = getGroundPlaneSize(family)
    if gps==0:
        return 0
    return cumulativeMemberSize(family)/gps

# if the average is greater than half the cardinality of the family
# their must exists an element that is common
def averagingCheck(family):
    k = averageOccurence(family)
    k = math.ceil(k)
    return k >= membersAmount(family)/2

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
    if isUnionClosed(c):
        return c
    else:
        return makeUnionClosed(c)

# make a family intersection-closed
def makeIntersectionClosed(family):
    c = family.copy()
    for m in family:
        for n in family:
            c.add(m.intersection(n))
    if isIntersectionClosed(c):
        return c
    else:
        return makeIntersectionClosed(c)


# checks if their is a member in the family that has only one of x and y 
def seperated(family, x, y):
    for m in family:
        if xor(x in m, y in m):
            return True
    return False

# checks if all elements are seperated
def isSeperating(family, output=False):
    U = getGroundPlane(family)
    for x in U:
        for y in U:
            if x is y:
                continue
            if not seperated(family, x,y):
                if output:
                    print(str(x)+" and "+str(y)+" are not seperated")
                return False
    return True

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


def getGroundPlaneSize(family):
    return len(getGroundPlane(family))

# finds the most common elements in the family
def mostOccuring(family, output=False):
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
    return m, n

# finds the least common elements in the family
def leastOccuring(family, output=False):
    a = getGroundPlane(family);
    m = set()
    n = math.inf
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
    return m, n

# checks if the most apparant element is in at least
# half of the members of the members of the family
def hasCommon(family):
    e, n = mostOccuring(family)
    return n>=len(family)/2

# checks if the least apparant element is in at most
# half of the members of the members of the family
def hasRare(family):
    e, n = leastOccuring(family)
    return n<=len(family)/2


# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
def powerset(aset):
    if len(aset)>=30:
        warnings.warn("The powerset of a set with cardinality>30 will create at least 1 bilion sets.")
        
    s = list(aset)
    p = set()
    for r in range(len(s)+1):
        p = p.union(set(frozenset(i) for i in combinations(s, r)))
    return p

# finds the minimal members
# that is, the members that do properly contain another member
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

# finds the maximal members
# that is, the members that are not properly contained in another member
# except for the ground plane
def maximalMembers(family):
    maximalset = set()
    k = len(getGroundPlane(family))
    for m in family:
        maximal = True
        for n in family:
            if len(n)<k and (not n is m):
                if m.issubset(n):
                    maximal = False
                    break
        if maximal:
            maximalset.add(m)
    return maximalset

# union of the minimal members
def maximalElements(family):
    maxElements = set()
    maxMembers = maximalMembers(family)
    for m in maxMembers:
        for e in m:
            maxElements.add(e)
    return maxElements

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
def inspectFamily(F, everything=False):
    k = membersAmount(F)
    gp = getGroundPlane(F)
    gpn = len(gp)
    uc = isUnionClosed(F)
    ic = isIntersectionClosed(F)
    mm = minimalMembers(F)
    me = minimalElements(F)
    maxm = maximalMembers(F)
    maxe = maximalElements(F)
    mo, mon = mostOccuring(F)
    lo, lon = leastOccuring(F)
    hc = mon >= k/2
    hr = lon <= k/2
    s = isSeperating(F)

    if k<=1:
        if everything:
            print("Trivial Family")
        return
      
    if uc and (not hc):
        everything=True
        print("COUNTER EXAMPLE TO FRANKS CONJECTURE")

    if ic and (not hr) :
        everything=True
        print("COUNTER EXAMPLE TO FRANKS CONJECTURE")

    if uc and len(me.intersection(mo))==0:
        everything=True
        print("COUNTER EXAMPLE TO SANDER&GIJS CONJECTURE")

    if everything:
        print("Family:")
        printFamily(F)
        print("Number of members:", k)
        print("Ground Plane:",gp)
        print("Ground Plane Size:",gpn)
        print("Seperating:", s)
        print("Average Occurence:",averageOccurence(F))
        print("Union Closed:", uc)
        print("Intersection Closed:", ic)
        print("Minimal Members:")
        printFamily(mm)
        print("Minimal Elements:", me)
        print("Maximal Members:")
        printFamily(maxm)
        print("Maximal Elements:", maxe)
        print("Most Occuring:", mo, mon)
        print("Least Occuring:", lo, lon)
        print("Has Common?:", hc)
        print("Has Rare?:", hr)
        print("Averaging Check : ", averagingCheck(F))
