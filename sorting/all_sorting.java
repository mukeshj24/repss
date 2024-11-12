package repss.sorting;

public class all_sorting {
    public static void swap(int[] arr, int index1, int index2) {
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    public static void print(int [] arr){

        for(int i=0; i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }

        System.out.println();

    }

    public static void bubble (int arr[]){
        int n=arr.length;
        boolean flag=false;

        for (int i=0; i<n;i++){
            for (int j=0; j<n-1-i;j++){
                flag=true;

                if (arr[j]>arr[j+1]){
                    swap(arr,j,j+1);    // arr with index which needs to swap 

                }
            }


            if (flag==false){
                break;
            }
        }

    }
    public static void selection(int arr[]){

        for (int i=0; i<arr.length;i++){
            int minPos=i;
            for (int j=i+1; j<arr.length;j++){
                if (arr[j]<arr[minPos]){
                    minPos=j;
                }
               
            }
            swap(arr, i, minPos); // arr with index which needs to swap 
        }

    }
    public static void insertion(int arr[]){

        for (int i=1; i<arr.length;i++){

            int curr=arr[i];
            int prev=i-1;

            while (prev>=0 && arr[prev]>curr){
                arr[prev+1]=arr[prev];
                prev--;
            }

            arr[prev+1]=curr;
        }

    }
    public static void counting(int arr[]){

        int count[]=new int[500];

        for (int i=0; i<arr.length;i++){
            count[arr[i]]+=1;
        }
        int index=0;
 
        for (int j=0; j<count.length;j++){
            if (count[j]>0){
                arr[index]=j;
                index++;
                count[j]--;
            }

        }

    }

    public static void main (String[] args){
        int arr[]={4,3,5,1,2};
        print(arr);
        // bubble(arr);
        // selection(arr);
        // insertion(arr);
        counting(arr);
        

        print(arr);


    }
    
}