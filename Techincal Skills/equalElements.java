// given an integer array a of size n. in 1 second you can increase a value of one by one .find the minimum time in second to make all elements of array equal.

public class equalElements {
    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 1};
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (max < arr[i]) {
                max = arr[i];
            }
        }
        int time = 0;
        for (int i = 0; i < arr.length; i++) {
            time += (max - arr[i]);
        }
        System.out.print(time);        
    }
}
