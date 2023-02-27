a = [[0] * 15 for i in range(5)]

for i in range(5):
    w = list(input())
    w_len = len(w)

    for j in range(w_len):
        a[i][j] = w[j]

    
for j in range(15):
    for i in range(5):
        if a[i][j] == 0:
            continue
        else:
            print(a[i][j],end='')