import sys

def get_wood(tree,height):
    total=0

    for i in tree: 
        if i>height:
            total += i-height
    return total

def find_max_wood(tree,M):
    left=0
    right=max(tree)
    result=0

    while left<=right:
        mid=(left+right)//2
        wood=get_wood(tree,mid)

        if wood>= M:
            result = mid
            left=mid+1
        else:
            right=mid-1
    return result


N,M=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))

answer=find_max_wood(tree,M)
print(answer)
