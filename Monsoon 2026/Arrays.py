import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    nA, nB = map(int, input().split())
    k, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    largestA = a[k-1]
    smallestB = b[nB - m]

    print("YES" if largestA < smallestB else "NO")

t = 1
for _ in range(t): solve()