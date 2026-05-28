def findMax(n, a, b):
    M = m = 0
    for j in range(n):
        newM = max(M - a[j], b[j] - m)
        newm = min(m - a[j], b[j] - M)
        M, m = newM, newm
    return M

# Inputs
N = int(input())
tests = []
for i in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tests.append([n, a, b])

# Outputs:
for i in range(N):
    print(findMax(tests[i][0], tests[i][1], tests[i][2]))