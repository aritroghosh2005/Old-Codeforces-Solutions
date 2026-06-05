import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    sumOfFrosts = 0
    bottleneck = float('inf')

    for i in range(1, n+1):
        sumOfFrosts += a[i-1]
        maxHeight = sumOfFrosts // i
        
        bottleneck = min(bottleneck, maxHeight)
        h = bottleneck
        print(h, end=' ')
    print()



t = int(input())
for _ in range(t): solve()
