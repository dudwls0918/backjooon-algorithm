import sys


n = int(sys.stdin.readline())
array =[]
for i in range(0,n,1):
    a=int(sys.stdin.readline())
    array.append(a)

array.sort()

for i in range(0,n,1):
    print(array[i])