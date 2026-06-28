import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Finding sums from backwards
    total = [0]*n # total[i] means summation of elements upto a[i] from right
    a[n-1] = max(a[n-1], b[n-1])
    total[n-1] = a[n-1]

    for i in range(n-2, -1, -1):
        a[i] = max(a[i], a[i+1], b[i])
        total[i] = total[i+1] + a[i]
    
    # Taking queries: sum of a[l....r] equals a[l] - a[r+1]
    total.append(0)
    answers = []
    for __ in range(q):
        l, r = map(int, input().split())
        left = total[l-1]
        right = total[r]
        answers.append(left - right)
    print(*answers)

t = int(input())
for _ in range(t): solve()