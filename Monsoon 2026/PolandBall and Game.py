import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, m = map(int, input().split())

    # Checking words of PolandBall
    words = []
    for __ in range(n):
        word = input()
        words.append(word)
    
    # Checking words of EnemyBall
    commonWords = 0
    for _ in range(m):
        word = input()
        if word in words: commonWords += 1
    
    # Finding condition
    pWins = n > m if commonWords%2==0 else n > m - 1
    print("YES" if pWins else "NO")

t = 1
for _ in range(t): solve()