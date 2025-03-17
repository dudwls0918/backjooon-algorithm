n = int(input())
array =[]
for i in range(0,n,1):
    a=int(input())
    array.append(a)

array.sort()

for i in range(0,n,1):
    print(array[i])