


import time
start=time.time()
def mergeArray(arr,s,end ) :

    mid=(s+end)//2
    len1=mid-s+1
    len2=end-mid

    first=[0]*len1  # first new array 
    second=[0]*len2 # second new array 
    
    # copy values

    oldArrayIndex=s
    for i in range (0,len1):
        first[i]=arr[oldArrayIndex]
        oldArrayIndex+=1 # increse the index  element  

    oldArrayIndex=mid+1
    for i in range (0,len2):
        second[i]=arr[oldArrayIndex]
        oldArrayIndex+=1 # increse the index  element 
    

    # merge TWO sorted array 

    index1=0
    index2=0
    oldArrayIndex=s

    while (index1<len1 and index2<len2):
        if (first[index1]<second[index2]):
            arr[oldArrayIndex]=first[index1]
            index1+=1
            oldArrayIndex+=1
        else:
            arr[oldArrayIndex]=second[index2]
            oldArrayIndex+=1
            index2+=1

    while (index1<len1):
        arr[oldArrayIndex]=first[index1]
        index1+=1
        oldArrayIndex+=1

    while (index2< len2):
        arr[oldArrayIndex]=second[index2]
        oldArrayIndex+=1
        index2+=1


def merge(arr,s,end):

    if (s >= end):
        return
     
    mid=(s+end)//2
    
    # left part  sort 
    merge(arr,0,mid)

    # right part sort
    merge(arr,mid+1,end)

    # merge both array

    mergeArray(arr,s,end)

    





arr=[5,4,3,1,2,4,65,545,64646,-22,3,26,3,23,66,622222]
print(arr)
s=0
end=len(arr)-1

merge(arr,s,end)

print(arr)

end=time.time()

diff=end-start
print(diff)
