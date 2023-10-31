V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))
    print(edgeList)

from disjointsets3 import DisjointSets

s = DisjointSets(V)

#Merge both

edgeList.sort(key = lambda a:a[2])
print(edgeList)
W = 0
edgeCount = 0
for u,v,w in edgeList:
    print(u,v,w)
    if s.findset(u) != s.findset(v): # check whether they belong to different groups
        # add weight w to total weight W
        W += w 
        # union u and v
        s.union(u,v) 
        # add 1 to edgecount since we union-ed u and v
        edgeCount += 1

if edgeCount >= V - 1: # a graph is connected when |E| = |V| - 1
    print("Connected")
    print(W) # print out total weight

else:
    print("Not Connected")