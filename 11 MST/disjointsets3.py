
class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n
        
    def findset(self, u): # find representative
        # if current u has no more parent, return u
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u,v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            # by default;
            # a will become the parent of b
            # and the rank of a will be incremented by 1
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1