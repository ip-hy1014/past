N,M = map(int,input().split())
a = [input() for _ in range(N)]
# 番号ごとに座標を分類。スタートは0、ゴールは10
group = []
for n in range(11):
  group.append([])
for i in range(N):
  for j in range(M):
    if a[i][j] == "S":
      n = 0
    elif a[i][j] == "G":
      n = 10
    else:
      n = int(a[i][j])
    group[n].append([i,j])
# cost[i][j]:数字を正しく通ってマス(i,j)にたどり着く最小移動回数
# 非常に大きい値で初期化しておく
INF = 10**18
cost = [[INF]*M for _ in range(N)]
# 初期条件。スタート地点の座標はgroup[0][0]
si,sj = group[0][0]
cost[si][sj] = 0
# nが小さい方から順に求めていく
for n in range(1,11):
  # 更新したいマスそれぞれについてループ
  for i,j in group[n]:
    # 数字がn-1であるマスを全て試す
    for i2,j2 in group[n-1]:
      cost[i][j] = min(cost[i][j],cost[i2][j2]+abs(i-i2)+abs(j-j2))
# ゴール地点の座標はgroup[10][0]
# ただしゴール地点のcostがINFであれば、到達不可能であるため-1を出力
gi,gj = group[10][0]
ans = cost[gi][gj]
if ans == INF:
  ans = -1
print(ans)