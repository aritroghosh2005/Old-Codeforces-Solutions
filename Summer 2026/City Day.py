import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    for i in range(n):
        rain = a[i]
        # Checking for left alignment
        left = all(a[j] > rain for j in range(max(0, i-x), i))

        if left:
            # Checking for right alignment
            right = all(a[j] > rain for j in range(i+1, min(i+y, n-1) + 1))
            if right: print(i+1); return

t = 1
for _ in range(t): solve()