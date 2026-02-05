public class TargetSum {
    public static void main(String[] args) {
        int[] arr = {1,2,5,8,9,11};
        int k= 6;

        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]+arr[j]==k){
                    System.out.println("Found the Pair");
                    break;
                }
            }
        }















        // HashMap<Integer, Integer> map = new HashMap<>();
        // for(int i=0;i<arr.length;i++){
        //     int complement = k - arr[i];
        //     if(map.containsKey(complement)){
        //         System.out.println("Yes");
        //     }
        //     map.put(arr[i], i);
        // }
    }    
}
