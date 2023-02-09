import sys
n = int(input())
score = list(map(int,sys.stdin.readline().split()))
max_score = max(score)

score = [i/max_score*100 for i in score]
print(sum(score)/n)