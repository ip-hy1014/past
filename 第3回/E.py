n,m,q = map(int,input().split())
g = [[False]*n for _ in range(n)]
for i in range(m):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  g[u][v] = True
  g[v][u] = True
c = list(map(int,input().split()))
for i in range(q):
  query = list(map(int,input().split()))
  if query[0]==1:
    x = query[1]
    x -= 1
    print(c[x])
    for i in range(n):
      if g[x][i]:
        c[i] = c[x]
  if query[0] == 2:
    x = query[1]
    y = query[2]
    x -= 1
    print(c[x])
    c[x] = y