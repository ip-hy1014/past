n,q = map(int,input().split())
g = [[False]*n for _ in range(n)]
for i in range(q):
  s = list(map(int,input().split()))
  a = s[1]-1
  if s[0]==1:
    b = s[2]-1
    g[a][b]=True
  if s[0]==2:
    for v in range(n):
      if g[v][a]:
        g[a][v]=True
  if s[0]==3:
    f = []
    for v in range(n):
      if g[a][v]:
        for w in range(n):
          if g[v][w] and w!=a:
            f.append(w)
    for w in f:
      g[a][w]=True
for i in range(n):
  for j in range(n):
    if g[i][j]:
      print("Y",end="")
    else:
      print("N",end="")
  print()