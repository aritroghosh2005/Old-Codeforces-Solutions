import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from functools import cache

@cache
def findOperations(n, numbers, operations=0):


    i = n-1
    while i>=0:
        if numbers[i] >= numbers[i-1] and numbers[i] >= numbers[i+1]:
            numbers[i] //= 2
            return(n, numbers, operations+1)


def solve():
    n = int(input())
    a = list(map(int, input().split()))



t = int(input())
for _ in range(t):
    solve()