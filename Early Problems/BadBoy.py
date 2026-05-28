import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from math import sqrt

def solve():
    n, m, i, j = map(int, input().split())
    print(1, 1, n, m)

t = int(input())
for _ in range(t):
    solve()