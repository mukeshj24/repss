package repss.sorting;
import java.util.*;

public class selectionSort{

    public static void selection(int arr[]){

        int n= arr.length;
        
        for (int i=0; i<n;i++){

            int minPos=i;

            for (int j=i+1; j<n;j++){
                if (arr[j]<arr[minPos]){
                    minPos=j;
                }

                int temp=arr[i];
                arr[i]=arr[minPos];
                arr[minPos]=temp;
            }
        }

    
    }

    public static void print(int arr[]){

        for (int i=0; i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }



    public static void main (String[] args){

        System.out.println("SELECTION Sort");

         int arr[]={5,4,3,2,1};
         print(arr);
        System.out.println();
        
         selection(arr);
         print(arr);

        
    }

}

