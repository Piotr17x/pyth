from itertools import combinations

def comb(it,r):
    return list(combinations(it,r))
zb1=comb(range(1,11),3)
print(zb1)
print(len(zb1))