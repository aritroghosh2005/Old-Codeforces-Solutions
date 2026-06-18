import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    paired = []

    for i in range(n-1):
        x, y = a[i], a[i+1]
        pdt = x*y
        if pdt%6 == 0: paired.append((i, i+1))

    


t = int(input())
for _ in range(t): solve()
