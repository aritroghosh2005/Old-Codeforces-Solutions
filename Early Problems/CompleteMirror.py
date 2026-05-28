from collections import deque

import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args))+'\n')

n = int(input())

neighbours = [ [] for _ in range(n+1)]
deg = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    neighbours[a].append(b)
    neighbours[b].append(a)

    deg[a] += 1
    deg[b] += 1

def findCentres(neighbours, n):
    if n==1: return [1]
    if n==2: return [1,2]

    degrees = [0]*(n+1)
    for i in range(1, n+1): degrees[i] = len(neighbours[i])

    leaves = deque()
    for i in range(1, n+1):
        if degrees[i]==1: leaves.append(i)

    remaining = n
    while remaining >2:
        newLeaves = deque()
        for _ in range(len(leaves)):
            leaf = leaves.popleft()
            remaining -= 1
            for neighbour in neighbours[leaf]:
                degrees[neighbour] -= 1
                if degrees[neighbour] == 1: newLeaves.append(neighbour)
        leaves = newLeaves
    return list(leaves)

def checkRoot(root):
    distances = [-1]*(n+1)
    distances[root] = 0

    queue = deque([root])
    while queue:
        current = queue.popleft()
        for neighbour in neighbours[current]:
            if distances[neighbour]==-1: 
                distances[neighbour] = distances[current] + 1
                queue.append(neighbour)
    
    levels = {}
    for node in range(1, n+1):
        d = distances[node]
        if d not in levels: levels[d] = set()
        levels[d].add(deg[node])

        if len(levels[d]) > 1: return False
    return True

centres = findCentres(neighbours, n)

for centre in centres:
    if checkRoot(centre):
        print(centre)
        exit()

centres = findCentres(neighbours, n)

visited = set()
queue = deque(centres)

for centre in centres:
    visited.add(centre)

while queue:
    node = queue.popleft()
    
    if checkRoot(node):
        print(node)
        exit()
    
    for neighbor in neighbours[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print(-1)