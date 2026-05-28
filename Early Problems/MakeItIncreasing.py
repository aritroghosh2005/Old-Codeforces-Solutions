import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def findOperations(n, a, mid, minOps):
    ops = 0
    b = [0]*(n+1)

    for i in range(mid-1, 0, -1):
        if b[i] >= b[i+1]:
            diff = b[i] - b[i+1] + 1
            num_ops = -(-diff//a[i])
            b[i] -= num_ops*a[i]
            ops += num_ops
            if ops > minOps: return minOps
        
    for i in range(mid+1, n+1):
        if b[i] <= b[i-1]:
            diff = b[i-1] - b[i] + 1
            num_ops = -(-diff//a[i])
            b[i] += num_ops*a[i]
            ops += num_ops
            if ops>minOps: return minOps
    
    return ops
        
n = int(input())
a = [0] + list(map(int, input().split()))

minOps = float('inf')

for mid in range(1, n+1):
    result = findOperations(n, a, mid, minOps)
    minOps = result
    
print(minOps)