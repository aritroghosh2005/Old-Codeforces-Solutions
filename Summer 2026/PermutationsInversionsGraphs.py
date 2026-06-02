import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    k = largestNow = 0
    for i in range(n):
        largestNow = max(p[i], largestNow)
        if largestNow == i+1: k += 1
    print(k)

t = int(input())
for _ in range(t): solve()
