#4
exam =  [99,78,100,91,81,85,54,100,71,50]
score = []
for n in exam:
  jumsu = n + 5
  if jumsu > 100:
    jumsu = 100
  score.append(jumsu)
print(score)

