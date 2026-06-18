import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())

    points = 0
    for deno in range(1, n+1):
        points += (1/deno)
    print(f"{points:.12f}")

t = 1 # int(input())
for _ in range(t): solve()
