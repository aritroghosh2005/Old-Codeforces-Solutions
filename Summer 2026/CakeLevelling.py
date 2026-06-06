import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    bottleneck = float('inf')
    sumOfFrostings = 0
    bottlenecks = []

    for i in range(n):
        sumOfFrostings += a[i]
        bottleneck = min(bottleneck, sumOfFrostings // (i+1))
        bottlenecks.append(bottleneck)
    print(*bottlenecks)

t = int(input())
for _ in range(t): solve()
