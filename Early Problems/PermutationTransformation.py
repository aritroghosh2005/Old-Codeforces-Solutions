import sys
input = lambda: sys.stdin.readline().rstrip()
output = lambda *args: sys.stdout.write(" ".join(map(str, args)) + '\n')

class Node:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        self.parent = None
    def display(self, level=0):
        print("  "*level+str(self.data))
        if self.left: self.left.display(level+1)
        if self.right: self.right.display(level+1)
    def depth(self):
        if not self.parent: return 0
        return 1 + self.parent.depth()

def buildTree(a, nodeMap):
    if not a: return None
    
    maxVal = max(a)
    i = a.index(maxVal)
    root = Node(maxVal)

    nodeMap[maxVal] = root

    leftRoot = buildTree(a[:i], nodeMap)
    rightRoot = buildTree(a[i+1:], nodeMap)

    if leftRoot:
        leftRoot.parent = root
        root.left = leftRoot
    if rightRoot:
        rightRoot.parent = root
        root.right = rightRoot

    return root

def findDepths(n,a):
    nodeMap = {}
    root = buildTree(a, nodeMap)
    depths = []
    for value in a:
        node = nodeMap[value]
        depths.append(node.depth())
    print(*depths)

t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    tests.append([n,a])

for _ in tests:
    findDepths(_[0], _[1])

