import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from collections import deque

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    neighbours = [ [] for _ in range(n)]
    for _ in range(n-1):
        u,v = map(int, input().split())
        u -= 1
        v -= 1
        neighbours[u].append(v)
        neighbours[v].append(u)

    queue = deque([0])
    visited = [True] + [False]*(n-1)
    children = [ [] for _ in range(n) ]

    while queue:
        node = queue.popleft()
        for neighbour in neighbours[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                children[node].append(neighbour)
                queue.append(neighbour)
    inTime = [0]*n
    outTime = [0]*n
    timer = 0

    mex1 = [0]*n
    mex2 = [0]*n

    pos = [0]*n
    for i in range(n): pos[p[i]] = i

    present = [False]*(n+2)
    
    stack = [(0,0,0,1)]
    mex1_val, mex2_val = 0, 1

    while stack:
        u, state, old_m1, old_m2 = stack.pop()
        if state == 0:
            inTime[u] = timer
            timer += 1
        


t = int(input())
for _ in range(t): solve()