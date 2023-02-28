a,b,v = map(int, input().split())
day = 0
r = v-a
if r == 0 : #남은 길이가 0이면(막대 = A 가 같으므로 0일)
    day = 0
elif r < (a-b): # 남은 길이가 (낮밤)하루 오르는 길이보다 짧으면 1일
    day = 1
else: # 남은 길이가 (낮밤)하루 오르는 길이보다 길면 나머지 + 1일
    if r % (a-b) == 0:
        day = r // (a-b) 
    else:
        day = r // (a-b) + 1
print(day + 1)