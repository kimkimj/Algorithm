package GreedyAlgorithm;

public class Budget {
    public static void main(String[] args) {
        int[] arr1 = {1,3,2,5,4};
        int[] arr2 = {2,2,3,3};
        System.out.println(numberOfDept(arr1, 9));
        System.out.println(numberOfDept(arr2, 10));
    }

    // greedy algorithm
    public static int numberOfDept(int[] d, int budget) {
        int count = 0;
        for (int i = 0; i < d.length; i++) {
            if (budget - d[i] < 0) {
                break;
            }
            count++;
            budget -= d[i];
        }
        return count;
    }
}
