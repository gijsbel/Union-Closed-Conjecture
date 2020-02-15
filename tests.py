from core import *

from random import randint

# family from list of lists
"""
F = [[1,2],[1],[3],[4,3],[4]]
F = familyFromList(F)
"""


# makes a random family
# and makes it union closed
"""
F = randomFamily(4,6)
F = makeUnionClosed(F)
"""


#prints information of a family
"""
printFamily(F)
print("union closed: ",isUnionClosed(F))
print("ground plane: ",getGroundPlane(F))
print("most apparant:",mostApparant(F),numberOfAppearances(F,mostApparant(F)))
print("common:",hasCommon(F))
"""


# Aproximately finds the amount of families that have a common element
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


#all kinds of bullshit
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
    mostApp     = mostOccuring(f)
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
"""

"""
n = 4
U = frozenset(range(1,n+1))
PU = powerset(U)
PPU = powerset(PU)
print("Their are ",len(PU)," members in total")
print("Their are ",len(PPU)," families in total")
uc = 0
ic = 0
ucic = 0

for f in PPU:
    iic = isIntersectionClosed(f)
    iuc = isUnionClosed(f)
    if iic:
        ic += 1
    if iuc:
        uc += 1
    if iic and iuc:
        ucic += 1

print(uc,ic,ucic)
"""


# this family is a counter-example to the non-theorem that
# The smallest(in cardinality) nonempty set contains
# an element that is in at least half the members.
"""
G1 = familyFromList([[],[1],[1,2,3]])
G2 = familyFromList([[],[2],[1,2,3]])
G3 = familyFromList([[],[3],[1,2,3]])

H1 = familyFromList([[5,6,7,8,9],[4,6,7,8,9]])
H2 = familyFromList([[4,5,7,8,9],[4,5,6,8,9]])
H3 = familyFromList([[4,5,6,7,9],[4,5,6,7,8]])

R1 = familyFromList([[],[1,2,3]])
R2 = powerset([1,2,3])
R3 = familyFromList([[4,5,6,7,8,9]])
                    
F = R1.union(mixFamilies(G1,H1))
F = F.union(mixFamilies(G2,H2))
F = F.union(mixFamilies(G3,H3))
F = F.union(mixFamilies(R2,R3))
inspectFamily(F)
"""


"""
n = 10
print("making powerset of universe...")
P = powerset(range(1,n+1))
print("power set has cardinality ",len(P))
print("done")
for i in range(10000):
    print(i)
    k = randint(3, len(P)/64)
    f = set(sample(P,k))
    #f = makeUnionClosed(f)
    inspectFamily(f)
"""


F = [[1,2],[1],[3],[4,3],[4]]
F = familyFromList(F)
inspectFamily(F)
