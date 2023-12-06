c = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
  c = c.replace(i, '*')

cnt = c.count('*') * 2
print(cnt)