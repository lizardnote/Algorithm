def solution(n, arr1, arr2):

    def make_bin(array,n):
        answer = []
        
        for i in array :
            arbin = bin(i)[2:]
            arbin = list(arbin.zfill(n))
            answer.append(arbin)
        return answer
    
    bin1 = make_bin(arr1,n)
    bin2 = make_bin(arr2,n)
    
    
    for i in range(n) :
        for j in range(n) :
            if bin1[i][j] != bin2[i][j] :
                bin1[i][j] = '1'   
        bin1[i] = (''.join(bin1[i]))
        bin1[i] = bin1[i].replace('1','#')
        bin1[i] = bin1[i].replace('0',' ')            
            
    
    return bin1
            