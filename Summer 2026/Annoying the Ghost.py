import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Check if going to order is possible
    aSorted = sorted(a)
    for i in range(n):
        if aSorted[i] > b[i]: print(-1); return

    # How many swaps to go to sorted ordering
    swaps = 0
    for i in range(n):
        for j in range(i, n):
            if a[j] <= b[i]: break
        # Swapping a[j] to b[i]
        val = a[j]
        a.pop(j)
        a.insert(i, val)
        swaps += (j-i)
    print(swaps)

t = int(input())
for _ in range(t): solve()
