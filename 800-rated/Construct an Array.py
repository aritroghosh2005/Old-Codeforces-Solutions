import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    
    array = list(range(1, 2*n, 2))
    print(*array)

t = int(input())
for _ in range(t): solve()
