import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ops = 0
    for i in range(1, n):
        if a[i]%2 == a[i-1]%2: ops += 1
    print(ops)

t = int(input())
for _ in range(t): solve()