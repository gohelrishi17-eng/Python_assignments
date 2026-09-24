scores = [45, 78, 102, 34, 67, 89]

i = 0

while i < len(scores):
    score = scores[i]

    if score > 100:
        break
    print(score)
    i+=1