import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, k = map(int, input().split())

    start, end = 1, 2**n - 1
    val = n

    while start <= end:
        mid = (start+end) // 2
        if k == mid: print(val); return
        elif k < mid: end = mid - 1
        else: start = mid + 1
        val -= 1

t = 1
for _ in range(t): solve()