import sys
input = lambda : sys.stdin.readline().rstrip()

from math import isqrt

def solve():
    k = int(input())

    start, mid, end = 0, 0, 2*(10**18)
    best = -1

    while start <= end:
        mid = (start+end)//2
        K = mid - isqrt(mid)

        if K > k: end = mid - 1
        elif K < k: start = mid + 1
        else:
            best = mid
            end = mid - 1 
    print(best)

t = int(input())
for _ in range(t): solve()
