import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    a1, a2 = map(int, input().split())
    time = 1 if (a1>=2 or a2>=2) else 0

    while a1>2 or a2>2:
        if a2>2: # First joystick charged until second on limit
            minutes = (a2-1)//2
            time += minutes
            a2 -= minutes*2
            a1 += minutes
        else: # Second joystick charged until first on limit
            minutes = (a1-1)//2
            time += minutes
            a1 -= minutes*2
            a2 += minutes
    print(time)

t = 1
for _ in range(t): solve()
