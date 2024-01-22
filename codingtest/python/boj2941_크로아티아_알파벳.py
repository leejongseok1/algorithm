c = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
  c = c.replace(i, '*')

print(len(c))