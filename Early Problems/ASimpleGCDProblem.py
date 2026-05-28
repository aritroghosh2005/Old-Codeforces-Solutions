import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from math import gcd, lcm
from itertools import pairwise 

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    op = 0
    g = [gcd(num1, num2) for num1, num2 in pairwise(a)]

    for i in range(n):
        leftGCD = g[i-1] if i>0 else 1
        rightGCD = g[i] if i<n-1 else 1
        target = lcm(leftGCD, rightGCD)
        if a[i] > target: op += 1
    print(op)
 
t = int(input())
for _ in range(t): solve()