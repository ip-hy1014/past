n,l = list(map(int,input().split()))
X = list(map(int,input().split()))
t1,t2,t3 = list(map(int,input().split()))

# ハードルがある座標においてTrueとなるような配列
h = [False]*(l+1)
for x in X:
  h[x] = True

# cost[i]:座標iで行動を終了するまでの最小所要時間
# 非常に大きな値で初期化しておき、minを用いて更新する
cost = [10**100]*(l+1)

# 初期条件
cost[0] = 0

# 順番に求めていく
for i in range(1,l+1):
  # 行動1
  cost[i] = min(cost[i],cost[i-1]+t1)
  # 行動2
  if i>=2:
    cost[i] = min(cost[i],cost[i-2]+t1+t2)
  # 行動3
  if i>=4:
    cost[i] = min(cost[i],cost[i-4]+t1+3*t2)
  # もしハードルがあれば加算
  if h[i]:
    cost[i] += t3

# 答えは座標lにピッタリ止まるか、座標(l-3)~(l-1)からジャンプ中にゴールしたもの
ans = cost[l]
for i in [l-3,l-2,l-1]:
  if i>=0:
    ans = min(ans,cost[i] + t1//2 + t2*(2*(l-i)-1)//2)
print(ans)