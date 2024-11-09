class Bubblesort:
    
   def bubble (self,arr):
      
      self.n=len(arr)
      flag=False  # to check swapping is necessary or not or already list is swaped 
      self.count=0
    
      for i  in range (0,self.n):
        for j in range (0,self.n-1-i):
            if (arr[j]>arr[j+1]):
                flag=True
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                self.count+=1

        if (flag==False):  # if the swaaping not happend it means loop is already sorted 
           break     # break statement break the innner  and outer both the  looop 

        
    

arr=[5,4,3,2,1]

print(arr)
sort=Bubblesort()
sort.bubble(arr)




print(arr)
print(sort.count)  # object k through acces kar sakta h fn ko 4
