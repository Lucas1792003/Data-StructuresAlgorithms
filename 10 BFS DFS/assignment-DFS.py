graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
print (adj_list)
color = ["WHITE"] * V
p = [None] * V
time = 0
d = [-1] * V
f = [-1] * V

# Depth-First Search
n = V  # Number of vertices
# inputAdj_List = [list(map(int, input().split())) for _ in range(n)]

color = ["WHITE"] * n
predecessor = [None] * n
d, f = [[-1] * n for _ in range(2)]
time = 0


def dfs_visit(u):
    global time
    time += 1
    d[u] = time
    color[u] = "GREY"

    for v in adj_list[u]:  # Iterating through adjacent vertices directly
        if color[v] == "WHITE":
            p[v] = u
            dfs_visit(v)

    color[u] = "BLACK"
    time += 1
    f[u] = time


def dfs():
    for i in range(n):
        if color[i] == "WHITE":
            dfs_visit(i)


dfs()
for v in range(n):
    print(v + 1, d[v], f[v])


# dfs(inputAdj_List)
# for v in range(n):
#     print(v + 1, d[v], f[v])

# Print additional information
for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    if p[v] is not None:
        pv = p[v] + 1
    else:
        pv = "None"

    print("%d %5s %5s %5s" % (v + 1, color[v], dv, fv), pv)
