import sys

def search(arr,K,start,end):
    result=0
    while start<=end:
        count=0
        mid=(start+end)//2

        for i in range(len(arr)):
            if arr[i]<mid:
                count += mid-arr[i]

        if count<=K:
            result=mid
            start=mid+1
    
        else:
            end=mid-1

    return result




N,K=map(int,sys.stdin.readline().split())
X=[]
for i in range(N):
    X.append(int(sys.stdin.readline()))
X.sort()
start=X[0]
end=X[N-1]+K
print(search(X,K,start,end))
