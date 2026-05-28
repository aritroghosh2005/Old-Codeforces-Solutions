import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from math import floor, sqrt

def solve():
    w,b = map(int, input().split())

    prod = 2*(w+b)
    st = floor(sqrt(prod))

    if st*(st+1) <= prod: print(st)
    else: print(st-1)

t = int(input())
for _ in range(t):
    solve()