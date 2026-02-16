import java.util.Scanner;

public class matrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter rows:");
        int row = sc.nextInt();
        System.out.println("Enter columns:");
        int col = sc.nextInt();
        
        int arr[][] = new int[row][col];
        
        System.out.println("-------------");
        for (int i=0; i< row; i++) {
            for (int j=0;j<col; j++) {
                System.out.println("Enter element at [" + i + "][" + j + "]:");
                arr[i][j] = sc.nextInt();
            }
        }

        System.out.println("-------------");
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[i].length;j++){
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (i == j) {  
                    sum += arr[i][j];
                }
            }
        }

        System.out.println("Sum of diagonal elements: " + sum);
    }
}
