# relative distance of above, below, left, and right cells
adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def valid(r, c):
    # return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall

    global steps

    if r >= 0 and r < 10 and c >= 0 and c < 10:
        if steps[r][c] == 0:
            return True
    return False

'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''

# Read input maze
maze = []
ends = []
for r in range(10):
    maze.append(input())

# Set up the steps matrix
steps = [[0] * 10 for r in range(10)]
for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1
        if maze[r][c] == 'X':
            ends.append((r, c))

# Breadth-First Search
Queue = []
Queue.append((ends[0], 0))
while Queue != []:
    (r, c), d = Queue[0]
    Queue = Queue[1:]
    for dr, dc in adj:
        rr, cc = r + dr, c + dc
        if valid(rr, cc):
            Queue.append(((rr, cc), d + 1))
            steps[rr][cc] = d + 1

# Calculate and print the distance between the two ends
distance = steps[ends[1][0]][ends[1][1]]
print(distance)
