import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from itertools import pairwise

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    op = 0
    toCheck = True
    for x,y in pairwise(a):
        if toCheck and (x==y or x+y==7): # Operation performed
            op+=1
            toCheck = False # No need to check next pair
        else: # No operation performed
            toCheck = True # Check next pair
    print(op)

t = int(input())
for _ in range(t): solve()