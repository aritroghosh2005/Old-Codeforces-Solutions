import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = ['$'] + list(map(int, input().split()))
    b = ['$'] + list(map(int, input().split()))
    c = ['$'] + list(map(int, input().split()))

    violatorsTorso = [ set() for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[j] <= a[i]: violatorsTorso[i].add(j)

    violatorsLeg = [ set() for _ in range(n+1)]
    for j in range(1, n+1):
        for k in range(1, n+1):
            if a[k] <= a[j]: violatorsLeg[j].add(k)
    
    i = 1
    triplets = 0
    for j, k

             



t = int(input())
for _ in range(t): solve()
