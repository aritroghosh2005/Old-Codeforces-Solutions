import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    m, M = min(a), max(a)
    ops = (M-m+1)//2
    print(ops)

t = int(input())
for _ in range(t): solve()
