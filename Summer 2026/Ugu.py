import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    s = input()

    disjoints = sum(s[i] != s[i+1] for i in range(n-1))
    if s[0] == '0': flips = max(disjoints - 1, 0)
    else: flips = disjoints
    print(flips)

t = int(input())
for _ in range(t): solve()
