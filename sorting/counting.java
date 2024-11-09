package repss.sorting;

public class counting {

    public static void Counting (int arr[]) {

        int count[]=new int[10000];
        for(int i=0; i<arr.length; i++){
            count[arr[i]]+=1;


        }
       int index=0;

        for (int j=0 ; j<count.length; j++){

            if (count[j]>0){
                arr[index]=j;
                count[j]--;
                index++;
            }


        }
        
    }
    public static void print(int arr[]){
        for (int i=0; i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }


    


    public static void main(String[] args) {

        System.out.println("Counting  sort ");
        int arr[]={5,4,3,1,2};
        print(arr);
        System.out.println();
        Counting(arr);

        print(arr);

        
    }
    
}
