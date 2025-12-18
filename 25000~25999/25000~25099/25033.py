"""
[25033: finitefunc](https://www.acmicpc.net/problem/25033)

Tier: Silver 5 
Category: data_structures, hash_set, set
"""


def finitefunc(D):
    return set(D.values())

######### SUBMIT THE ABOVE CODE ONLY #########

print(finitefunc({})) # set()
print(finitefunc({1:2})) # {2}
print(finitefunc({3:-4,8:-100,-5:-4,6:85})) # {-100, -4, 85}
print(finitefunc({i:i%4 for i in range(-500,500)})) # {0, 1, 2, 3}
