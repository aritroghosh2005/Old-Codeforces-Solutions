import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    if freq[0]==0: print("NO")
    elif freq[0]==1: print("YES")
    else:
        if 1 in a: print("YES")
        else: print("NO")

t = int(input())
for _ in range(t): solve()