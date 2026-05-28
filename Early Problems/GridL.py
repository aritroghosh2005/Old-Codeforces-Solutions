import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from math import sqrt

def solve():
    p,q = map(int, input().split())
    totalSticks = p + 2*q

    target = 2*totalSticks + 1
    maxTarget = int(target**0.5)

    for i in range(3, maxTarget + 1, 2):
        if target%i==0: 
            A, B = i, target // i
            n, m = (A-1)//2, (B-1)//2
            if q <= min(m*(n+1), n*(m+1)): 
                print(n, m)
                break
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()