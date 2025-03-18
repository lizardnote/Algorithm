from itertools import permutations

def solution(k, dungeons):
    dun_list = list(permutations(dungeons,len(dungeons)))  
    cnt_list = []
    for i in dun_list:
        cnt = 0
        kk = k
        for j in i:
            if kk >= j[0]:
                kk -= j[1]
                cnt += 1
            cnt_list.append(cnt)
    
    return max(cnt_list)