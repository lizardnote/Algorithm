n = int(input())

def soinsu(n):
    d = 2
    while d <= n:
        if n % d == 0:
            print(d)
            n = n/d
        else:
            d += 1
soinsu(n)    