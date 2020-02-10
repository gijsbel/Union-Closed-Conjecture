from core import *


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
"""


n = 3
U = frozenset(range(1,n+1))
PU = powerset(U)
PPU = powerset(PU)
print("Their are ",len(PU)," members in total")
print("Their are ",len(PPU)," families in total")
for f in PPU:
    if isUnionClosed(f):
        if isIntersectionClosed(f):
            scf = superComplementFamily(f, PU)
            if not isIntersectionClosed(scf):
                if not isUnionClosed(scf):
                    printFamily(f)
                    printFamily(scf)
