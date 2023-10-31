graph_type = input()
V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]

for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

color = ["WHITE"] * V
d = [-1] * V
p = [None] * V

# Breadth-First Search
n = V  # The number of vertices
s = 0  # Starting vertex

color[s] = "GREY"
d[s] = 0
p[s] = None

Q = [s]
while Q:
    u = Q[0]
    del Q[0]

    for v in adj_list[u]:
        if color[v] == "WHITE":
            color[v] = "GREY"
            d[v] = d[u] + 1
            p[v] = u
            Q.append(v)

    color[u] = "BLACK"

# Output BFS results
for v in range(n):
    print(v + 1, d[v])

# Print additional information
for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] is not None:
        pv = p[v] + 1
    else:
        pv = "None"

    print("%d %5s %5s" % (v + 1, color[v], dv), pv)
