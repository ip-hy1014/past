from collections import Counter
s = input()
c = Counter(s)
print(c.most_common()[0][0])