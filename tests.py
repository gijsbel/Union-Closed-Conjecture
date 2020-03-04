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



n = 4
U = frozenset(range(1,n+1))
PU = powerset(U)
PPU = powerset(PU)
print("Their are ",len(PU)," members in total")
print("Their are ",len(PPU)," families in total")

c = 0
m = 0
s = 0
for f in PPU:
    if isUnionClosed(f) and isIntersectionClosed(f):
        c += 1
        if isMinimal(f):
            m += 1
        if isSeperating(f):
            s += 1
print(c, m, s)



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
