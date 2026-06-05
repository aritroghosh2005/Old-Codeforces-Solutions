import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    calls = 0
    a.sort()

    for i in range(n//2):
        f1, f2 = a[i], a[n-i-1]
        if f1 != f2: calls += 1
    print(calls)

t = int(input())
for _ in range(t): solve()
