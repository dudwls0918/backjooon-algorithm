import sys

def function(a,b,c):
    if b == 1:
        return a%c
    if b % 2 ==0:
        return(function(a,b//2,c)**2)%c
    else:
        return((function(a,b//2,c)**2)*a)%c

a,b,c=map(int,sys.stdin.readline().split())
print(function(a,b,c))