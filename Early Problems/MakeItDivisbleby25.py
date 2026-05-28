import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve(num):
    n = len(num)
    minOperations = float('inf')

    for ending in ['00', '25', '50', '75']:
        operations = 0
        L = ending[-1]
        L2 = ending[0]
        pos1 = pos2 = -1

        for i in range(n-1, -1, -1):
            if num[i] == L: 
                pos1 = i
                break
            else: operations += 1
        
        for i in range(pos1-1, -1, -1):
            if num[i]==L2:
                pos2 = i
                break
            else: operations += 1

        if operations<minOperations: minOperations = operations
    print(minOperations)

t = int(input())
for _ in range(t):
    num = input() # Input number as string
    solve(num)