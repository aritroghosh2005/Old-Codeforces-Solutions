import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    hC, dC = map(int, input().split())
    hM, dM = map(int, input().split())
    k, w, a = map(int, input().split())
    
    # Let Monocarp use 'p' armour upgrades and 'q' weapon upgrades
    for p in range(0, k+1):
        q = k - p

        h = hC + p*a
        d = dC + q*w
        
        x, y = (hM + d -1)//d, (h+dM-1)//dM
        if x <= y: print("YES"); return
    print("NO")

t = int(input())
for _ in range(t): solve()