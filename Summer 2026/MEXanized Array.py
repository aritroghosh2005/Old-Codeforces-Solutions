import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, k, x = map(int, input().split())
    if k > n or k-1 > x: print(-1)
    else:
        total = 0
        # Fill with 0 to (k-1)
        for i in range(0, k): total += i

        # If all places not filled, fill with highest possible number excluding 
        if n > k: 
            highestNumber = x if x > k else (k-1)
            total += highestNumber*(n-k)
        print(total)

t = int(input())
for _ in range(t): solve()