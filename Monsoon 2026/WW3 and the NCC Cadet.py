import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque
"""
def setParents(root, parents, neighbours, visited):

    visited.add(root)
    if not neighbours[root]: return

    for node in neighbours[root]:
        if node not in visited:
            parents[node] = root
            setParents(node, parents, neighbours, visited)
"""

def solve():
    n, r1, r2 = map(int, input().split())
    pp = list(map(int, input().split()))

    # Setting original parents
    index = 0
    neighbours = [[] for lom in range(n+1)] # parents[i] means parent of i
    for i in range(1, n+1):
        if i == r1: continue
        p = pp[index]
        neighbours[i].append(p)
        neighbours[p].append(i)
        index += 1
    
    # Finding new parents using DFS
    parents = [ [] for lom in range(n+1) ] # newParents[i] means parent of node i
    visited = set()

    queue = deque([r2])
    while queue:
        root = queue[0]
        visited.add(root)

        if neighbours[root]:
            for neighbour in neighbours[root]:
                if neighbour not in visited:
                    parents[neighbour] = root
                    queue.append(neighbour)
        queue.popleft()
    
    for i in range(1, n+1):
        if i != r2: print(parents[i], end=' ')
    print()        

t = 1
for _ in range(t): solve()