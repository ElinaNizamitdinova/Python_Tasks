import math
import random
planets= [(random.randint(1,15),random.randint(1,15)) for _ in range(5)]
#planets= [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(planets)

def find_farthest_orbit(list_of_orbits):
    maxS=max_index=0
    for i,item in enumerate(list_of_orbits):
        a,b= item
        print(a,b)
        if math.pi*a*b>maxS and a!=b:
            maxS=math.pi*a*b
            s=[]
            max_index=i
    return list_of_orbits[max_index]


max_ordit= find_farthest_orbit(planets)
print(max_ordit)