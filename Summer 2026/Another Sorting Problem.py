import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    k = -1
    for i in range(1, n):
        if a[i] < a[i-1]: k = max(k, a[i-1] - a[i])

    for i in range(1, n):
        if a[i] < a[i-1]: a[i] += k
    
    if any(a[i] < a[i-1] for i in range(1, n)): print("NO")
    else: print("YES")

t = int(input())
for _ in range(t): solve()
