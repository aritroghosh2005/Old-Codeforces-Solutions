import sys
input = lambda : sys.stdin.readline().rstrip()

from math import inf

def solve():
    n = int(input())
    q = list(map(int, input().split()))

    # For it to be possible, q[i] cannot be (i-1) or less
    for i in range(n):
        if q[i] <= i: print(-1); return

    p = [0]*n
    p[0] = q[0]

    seen = {q[0]}
    # Fill the places where max rises
    for i in range(1, n):
        if q[i] > q[i-1]: 
            p[i] = q[i] # Max rises
            seen.add(q[i])

    # Find residues:
    residues = iter([num for num in range(1, n+1) if num not in seen])

    # Put residue in gaps in any order
    for i in range(n):
        if p[i] == 0: p[i] = next(residues)
    print(*p)

t = int(input())
for _ in range(t): solve()
