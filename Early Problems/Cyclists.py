import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, k, p, m = map(int, input().split())  
    a = [0]  
    a.extend(list(map(int, input().split())))  
    wins = 0

    while True:  
        if p <= k:
            if m >= a[p]:  
                wins += 1
                m -= a[p]
                a.append(a.pop(p))
                p = n
            else: break  
        else:
            card = min(a[1:k+1])  
            i = a[1:k+1].index(card) + 1  
            
            if m >= a[i]:  
                m -= a[i]
                a.append(a.pop(i))
                p -= 1
            else: break 
    print(wins)

t = int(input())
for _ in range(t):
    solve()