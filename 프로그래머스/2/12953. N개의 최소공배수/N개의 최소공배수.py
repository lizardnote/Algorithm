def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def solution(arr):
    arr.sort()
    temp = 1
    for i in range(len(arr)-1):
        temp = temp * arr[i+1] / gcd(temp, arr[i+1])
    
    return temp

