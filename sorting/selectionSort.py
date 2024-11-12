
class SelectionSort:

    

    def selection(self, arr):

        n=len(arr)

        for i in range (0,n):

            minPos=i

            for j in range (i+1, n):
                if(arr[j]<arr[minPos]):
                    minPos=j
                

            temp=arr[i]
            arr[i]=arr[minPos]
            arr[minPos]=temp

arr=[5,4,3,2,1]
print(arr)
sort= SelectionSort()
sort.selection(arr)
print(arr)

