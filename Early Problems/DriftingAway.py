def findTime(s):
    time = 0
    if ("*<" in s) or (">*" in s) or ("><" in s) or ("**" in s): time = -1
    else:
        lefts = s.count('<')
        rights = s.count('>')
        time = max(lefts, rights) +1 if "*" in s else max(lefts, rights)
    print(time)

N = int(input())
tests = []
for _ in range(N):
    tests.append(input())

for _ in range(N):
    findTime(tests[_])