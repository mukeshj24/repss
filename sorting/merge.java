package repss.sorting;
public class merge{

    public static void sortArray(int arr[],int s, int end ){

        int mid=(s+end)/2;
        int len1=mid-s+1;
        int len2=end-mid;

        int first[]=new int[len1];
        int second[]=new int [len2];

        //copy in the array 
        int oldIndex=s;
        for(int i=0; i<len1; i++){
            first[i]=arr[oldIndex];
            oldIndex++;
        }
        oldIndex=mid+1;
        for(int i=0; i<len2; i++){
            second[i]=arr[oldIndex];
            oldIndex++;
        }

        oldIndex=s;
        
        int index1=0;
        int index2=0;

        while (index1<len1 && index2<len2){
            if (first[index1]<second[index2]){
                arr[oldIndex]=first[index1];
                oldIndex++;
                index1++;
            }

            else {
                arr[oldIndex]=second[index2];
                oldIndex++;
                index2++;

            }
        }

        while (index1<len1){
            arr[oldIndex]=first[index1];
                oldIndex++;
                index1++;

        }

        while (index2<len2){
            arr[oldIndex]=second[index2];
                oldIndex++;
                index2++;

        }





    }

    public static  void mergeSort(int arr[],int s,int end){
        if (s>=end){
            return ;
        }
        int mid =(s+end)/2;

        //left part
        mergeSort(arr,s,mid);
        //right part 
        mergeSort(arr,mid+1,end);

        //sort
        sortArray(arr,s,end);

    }


    public static void main (String[] args ){
     
        int arr[]={5,4,3,1,2};

        for (int i=0; i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        int s=0;
        int end=arr.length-1;

        mergeSort(arr,s,end);

        System.out.print("\n")
        ;

        for (int i=0; i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }

    }
}