import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, x1, x2, k = map(int, input().split())

    dist1 = abs(x2-x1)
    dist2 = n - dist1
    dist = min(dist1, dist2)

    if n <= 3: print(dist)
    else: print(dist+k)

t = int(input())
for _ in range(t): solve()