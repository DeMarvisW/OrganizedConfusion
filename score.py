scores = []
for i in range(3):
    score = int(input("Scores: "))
    scores.append(score)
#rather than .append you may use "scores += [score]" to add to the empty list titled "scores".

average = sum(scores) / len(scores)
print(f"Average: {average}")
