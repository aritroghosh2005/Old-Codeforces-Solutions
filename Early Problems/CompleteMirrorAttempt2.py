import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    if n == 1:
        print(1)
        return
        
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
        
    def find_farthest(start):
        dist = [-1] * (n + 1)
        parent = [0] * (n + 1)
        dist[start] = 0
        
        q = deque([start])
        farthest_node = start
        max_d = 0
        
        while q:
            curr = q.popleft()
            if dist[curr] > max_d:
                max_d = dist[curr]
                farthest_node = curr
                
            for nxt in adj[curr]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[curr] + 1
                    parent[nxt] = curr
                    q.append(nxt)
                    
        return farthest_node, max_d, parent

    end1, _, _ = find_farthest(1)
    end2, diameter_len, parent_map = find_farthest(end1)
    
    path = []
    curr = end2
    while curr != 0:
        path.append(curr)
        curr = parent_map[curr]
        
    centers = []
    if diameter_len % 2 == 0:
        centers.append(path[diameter_len // 2])
    else:
        centers.append(path[diameter_len // 2])
        centers.append(path[diameter_len // 2 + 1])
        
    candidates = set(centers)
    
    for c in centers:
        length_to_leaf = {}
        
        for neighbor in adj[c]:
            curr = neighbor
            prev = c
            path_len = 1
            
            while deg[curr] == 2:
                next_dot = adj[curr][0] if adj[curr][0] != prev else adj[curr][1]
                prev = curr
                curr = next_dot
                path_len += 1
                
            if deg[curr] == 1:
                length_to_leaf[path_len] = curr
                
        for leaf in length_to_leaf.values():
            candidates.add(leaf)
            
    def check_is_valid(root_candidate):
        dist = [-1] * (n + 1)
        dist[root_candidate] = 0
        q = deque([root_candidate])
        levels = {}
        
        while q:
            curr = q.popleft()
            d = dist[curr]
            
            if d not in levels:
                levels[d] = deg[curr]
            elif levels[d] != deg[curr]:
                return False  
                
            for nxt in adj[curr]:
                if dist[nxt] == -1:
                    dist[nxt] = d + 1
                    q.append(nxt)
        return True

    for cand in candidates:
        if check_is_valid(cand):
            print(cand)
            return
            
    print("-1")

solve()