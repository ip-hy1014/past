n = int(input())
s = []
for i in range(n):
  s.append(list(input()))
for i in range(n-2,-1,-1):
  for j in range(1,2*n-1):
    if s[i][j] == "#":
      if s[i+1][j-1] == "X":
        s[i][j] = "X"
      elif s[i+1][j] == "X":
        s[i][j] = "X"
      elif s[i+1][j+1] == "X":
        s[i][j] = "X"
for i in range(n):
  print("".join(s[i]))