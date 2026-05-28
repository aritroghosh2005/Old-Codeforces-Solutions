import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    tasks = []
    for _ in range(n):
        c, p = map(int, input().split())
        tasks.append((c, p))
    
    g = 0.0
    for c, p in reversed(tasks):
        g = max(g, c + (1 - p / 100) * g)
    
    print(f"{g:.10f}")

t = int(input())
for _ in range(t):
    solve()