import sys
input = lambda : sys.stdin.readline().rstrip()

from collections import deque

def solve():
    n = int(input())

    neighbours = [ [] for _ in range(n+1) ]
    roadpoints = []
    for __ in range(n-1):
        a,b = map(int, input().split())
        neighbours[a].append(b)
        neighbours[b].append(a)
        roadpoints.append((a,b))

    maxProfit = 0
    for a,b in roadpoints:
        # Skip leaves
        if len(neighbours[a]) == 1 or len(neighbours[b]) == 1: continue

        # Temporarily remove the path
        neighbours[a].remove(b)
        neighbours[b].remove(a)

        # Finding longest path in component of 'a' starting from 'a'
        visited = set()
        queue = deque([(a,0)])
        road1 = 0

        while queue:
            val = queue.popleft()
            root, length = val[0], val[1]
            visited.add(root)
            road1 = max(road1, length)

            if neighbours[root]:
                for neighbour in neighbours[root]:
                    if neighbour not in visited:
                        queue.append((neighbour, length+1))

        # Finding longest path in component of 'a' starting from any other place
        visitedCopy = visited.copy()
        for potentialRoot in visitedCopy:
            visited = set()
            queue = deque([(potentialRoot,0)])

            while queue:
                val = queue.popleft()
                root, length = val[0], val[1]
                visited.add(root)
                road1 = max(road1, length)

                if neighbours[root]:
                    for neighbour in neighbours[root]:
                        if neighbour not in visited:
                            queue.append((neighbour, length+1))

        # Finding longest path in component of 'b'
        visited = set()
        queue = deque([(b,0)])
        road2 = 0

        while queue:
            val = queue.popleft()
            root, length = val[0], val[1]
            visited.add(root)
            road2 = max(road2, length)

            if neighbours[root]:
                for neighbour in neighbours[root]:
                    if neighbour not in visited:
                        queue.append((neighbour, length+1))
        
        # Finding longest path in component of 'b' starting from any other place
        visitedCopy = visited.copy()
        for potentialRoot in visitedCopy:
            visited = set()
            queue = deque([(potentialRoot,0)])

            while queue:
                val = queue.popleft()
                root, length = val[0], val[1]
                visited.add(root)
                road2 = max(road2, length)

                if neighbours[root]:
                    for neighbour in neighbours[root]:
                        if neighbour not in visited:
                            queue.append((neighbour, length+1))
        
        # Finding profit if this road is removed
        profit = road1*road2
        maxProfit = max(profit, maxProfit)

        # Repair the removed road
        neighbours[a].append(b)
        neighbours[b].append(a)
    print(maxProfit)
            
t = 1
for _ in range(t): solve()