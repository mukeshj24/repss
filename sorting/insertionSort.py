

class InsertionSort:
  def insertion (self,arr):
    n=len(arr)

    for i in range (1,n):
      curr=arr[i]
      prev=i-1

      while (prev >=0 and arr[prev]>curr):
        arr[prev+1]=arr[prev]   
        prev-=1

    #insertion code 
      arr[prev+1]=curr

  

arr=[5,4,3,2,1]

print(arr)

sort=InsertionSort()
sort.insertion(arr)
print(arr)
