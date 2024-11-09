package repss.sorting;
import java.util.*;


public class bubbleSort{


    public static void bubble(int[] arr){
        int n= arr.length;

        for (int i=0; i<n-1;i++){
            for (int j=0; j<n-i-1;j++){
                
                if (arr[j]> arr[j+1]){
                    int temp= arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;

                }
            }
        }
    }

    public static void print(int arr[]){
        for (int i=0; i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }
    public  static void main (String [] args){

    
        System.out.print("****Bubble sort logic \n logic start  from 0 and send the element  and if element is bigeer then swap the position ");

        int arr[]={5,4,3,1,2};


        print(arr);
        System.out.println();
        bubble(arr);

        print(arr);





    }

}
