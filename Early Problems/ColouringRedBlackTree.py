import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from collections import deque

def solve():
    n = int(input())
    s = ' ' + input()
    
    neighbours = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        neighbours[u].append(v)
        neighbours[v].append(u)
        degree[u] += 1
        degree[v] += 1
        
    order = []
    parent = [0] * (n + 1)
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbour in neighbours[node]:
            if neighbour != parent[node]:
                parent[neighbour] = node
                queue.append(neighbour)               
    order.reverse()
    
    dp = [[0.0, 0.0] for _ in range(n + 1)]
    
    for node in order:
        if s[node] == '1':
            childSum = 0.0
            for neighbour in neighbours[node]:
                if neighbour != parent[node]: childSum += dp[neighbour][1]    
            dp[node][0] = dp[node][1] = childSum
            
        else:
            tot0 = 0.0
            deltas = []
            
            for neighbour in neighbours[node]:
                if neighbour != parent[node]:
                    tot0 += dp[neighbour][1]
                    deltas.append(dp[neighbour][0] - dp[neighbour][1]) 
                                       
            deltas.sort()
            
            dp[node][0] = dp[node][1] = float('inf')
            delta = 0.0
            
            for i in range(len(deltas)+1):                    
                if i > 0:
                    delta += deltas[i-1]
                    costNode = degree[node] / i
                    dp[node][0] = min(dp[node][0], tot0 + delta + costNode)
                    
                costNodeWithParent = degree[node] / (i + 1)
                dp[node][1] = min(dp[node][1], tot0 + delta + costNodeWithParent)
                     
    print(f"{dp[1][0]:.12f}")

t = int(input())
for _ in range(t): solve()