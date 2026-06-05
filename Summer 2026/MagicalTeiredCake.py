import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    for m in range(1, n+1):
        if a[m-1] >= m: print("NO"); return
    
    pos = [1]*(n+1)
    moves = []

    def arrange(m, target):
        if m==0: return

        if pos[m] == target[m]: arrange(m-1, target)
        else:
            aux = 6 - pos[m] - target[m]
            neededOnTop = a[m-1]

            newTarget = target.copy()
            newTarget[1: m-neededOnTop] = [aux]*(m-neededOnTop-1)
            newTarget[m-neededOnTop:m] = [pos[m]]*neededOnTop

            arrange(m-1, newTarget)
            moves.append([m, pos[m], target[m]])
            pos[m] = target[m]

            arrange(m-1, target)
    
    target = [3]*(n+1)
    arrange(n, target)

    print("YES")
    print(len(moves))
    for move in moves: print(*move)

t = int(input())
for _ in range(t): solve()
