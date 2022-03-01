n = int(input())
c = list(map(int,input().split()))
q = int(input())

#合計販売枚数を記録
ans = 0

#全種類販売で販売した1種類あたりの枚数
z = 0

#セット販売で販売した1種類あたりの枚数
s = 0

#セット販売対象のcの最小値を記録
min_sc = 1000000000

#セット販売対象ではないcの最小値を記録
min_zc = 1000000000

for i in range(n):
  if i%2==0:
    min_sc = min(c[i],min_sc)
  else:
    min_zc = min(c[i],min_zc)

for _ in range(q):
  query = list(map(int,input().split()))
  if query[0]==1: #単品販売
    x = query[1] - 1
    a = query[2]
    #カードxの残枚数を計算
    if x%2==0:
      #セット販売対象のカードの場合
      card_x = c[x]-z-s
    else:
      card_x = c[x]-z
    #カードxがa枚いじょう残っていればa枚売る
    if card_x >= a:
      c[x] -= a
      ans += a
      if x%2==0:
        min_sc = min(c[x],min_sc)
      else:
        min_zc = min(c[x],min_zc)
  elif query[0]==2: #セット販売
    a = query[1]
    #偶数となるc[i]の最小値がa枚以上あるか調べる
    #a枚以上の場合a枚ずつ売る
    if min_sc-s-z >= a:
      s += a
  elif query[0]==3: #全種類販売
    a = query[1]
    #cの最小値がa枚以上あるか調べる
    #a枚以上の場合a枚ずつ売る
    if min(min_sc-s-z,min_zc-z) >= a:
      z += a
#セット販売した枚数を合算
for i in range(n):
  if i%2==0:
    ans += s
#全種類販売した枚数を合算
ans += z*n

print(ans)