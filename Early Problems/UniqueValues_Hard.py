import sys
input = lambda: sys.stdin.readline().rstrip()
#print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())

    low, high = 1, 2*n + 1
    while low < high:
        mid = (low + high)//2
        scoop = list(range(1, mid+1))

        print("?", len(scoop), *scoop, flush=True)
        count = int(input())
        if count == -1: return

        if (len(scoop) - count) & 1: high = mid
        else: low = mid + 1

    index3 = low

    low, high = 1, index3 - 1
    while low < high:
        mid = (low + high)//2
        scoop = list(range(1, mid+1))
        scoop.append(index3)

        print("?", len(scoop), *scoop, flush=True)
        count = int(input())
        if count == -1: return

        if (len(scoop) - count) & 1: high = mid
        else: low = mid + 1
    index2 = low

    low, high = 1, index2 - 1

    while low < high:
        mid = (low+high)//2
        scoop = list(range(1, mid+1))
        scoop.extend([index2, index3])

        print("?", len(scoop), *scoop, flush=True)
        count = int(input())
        if count==-1: return

        if (len(scoop)-count) & 1: high = mid
        else: low = mid + 1
    index1 = low

    print("!", index1, index2, index3, flush=True)

t = int(input())
for _ in range(t):
    solve()