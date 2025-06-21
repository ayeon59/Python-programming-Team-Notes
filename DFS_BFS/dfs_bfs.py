from collections import deque
n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(n):
    graph[j].sort()

def dfs(c):
    visited[c] = 1
    ans_dfs.append(c)
    for next in graph[c]:
        if not visited[next] :
            dfs(next)

def bfs(c):
    q = deque([c])
    visited[c] = 1
    ans_bfs.append(c)
    while q :
        node = q.popleft()
        for next in graph[node] :
            if not visited[next]:
                visited[next] = 1
                ans_bfs.append(next)
                q.append(next)


visited = [False] * (n+1)
ans_dfs = []
dfs(v)
print(*ans_dfs)

visited = [False] * (n+1)
ans_bfs = []
bfs(v)
print(*ans_bfs)
