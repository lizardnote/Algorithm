alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                 'o', 'p', 'q', 'r', 's', 't', 'u', 
                 'v', 'w', 'x', 'y', 'z']
word = list(input())

for i in alpha : 
    if i in word:
        print(word.index(i))
    else : 
        print(-1)