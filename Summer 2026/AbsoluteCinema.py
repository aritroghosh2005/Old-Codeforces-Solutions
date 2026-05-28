import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        if a[i] > b[i]: a[i], b[i] = b[i], a[i]
    val = max(a) + sum(b)
    print(val)

t = int(input())
for _ in range(t): solve()
