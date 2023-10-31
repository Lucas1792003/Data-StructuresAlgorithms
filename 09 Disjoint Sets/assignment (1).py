class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

ds = DisjointSets(10)  

# Define the edge list 
edge_list = [[0, 1], [0, 2], [1, 2], [1, 3], [4, 5], [4, 6], [7, 8], [9, 9]]

for edge in edge_list:
    u, v = edge
    ds.union(u, v)

def count_sets(ds):
    x = set() 
    for i in range(len(ds.p)):  
        y = ds.findset(i) 
        x.add(y)  
    return len(x)  


num_sets = count_sets(ds)
print("Number of disjoint sets:", num_sets)
