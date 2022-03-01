def is_match(t,s):
  for i in range(len(s)-len(t)+1):
    ok = True
    for j in range(len(t)):
      if s[i+j] != t[j] and t[j] != ".":
        ok = False
    if ok:
      return True
  return False
s = input()
a = "abcdefghijklmnopqrstuvwxyz."
l = []
for t in a:
  if is_match(t,s):
    l.append(t)
for a1 in a:
  for a2 in a:
      t = a1+a2
      if is_match(t,s):
        l.append(t)
for a1 in a:
  for a2 in a:
    for a3 in a:
      t = a1+a2+a3
      if is_match(t,s):
        l.append(t)
print(len(l))