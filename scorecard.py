
n = int(input())  
scores = list(map(int, input().split()))  


unique_scores = list(set(scores))
unique_scores.sort(reverse=True)


runner_up_score = unique_scores[1]
print(runner_up_score)