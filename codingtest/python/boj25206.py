grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_score = 0
total_credit = 0 # 학점

for i in range(20):
  a = list(map(str, input().strip().split()))
  credit = float(a[1])
  if a[2] == "P":
    continue
  else:
    idx = grade_list.index(a[2])
    score = score_list[idx]
    total_score += (credit * score)
    total_credit += credit

avg_score = float(total_score / total_credit)
print(avg_score)