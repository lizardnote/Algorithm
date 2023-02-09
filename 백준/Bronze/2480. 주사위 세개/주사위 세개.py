import sys
a,b,c = map(int, sys.stdin.readline().split())

if a == b and b == c :
    print(10000 + a * 1000)
elif a != b and a != c and b != c :
    print( max(a,b,c) * 100)
else:
    if a == b :
        print( 1000 + a*100 )
    elif a == c :
        print( 1000 + a*100 )        
    else : # b==c       
        print( 1000 + b*100 )        
    