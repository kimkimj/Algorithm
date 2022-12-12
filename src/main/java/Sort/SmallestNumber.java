package Sort;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SmallestNumber {
    public static void main(String[] args) {
        int[] arr = {4,3,2,1};
        int[] arr2 = {10};
        System.out.println(Arrays.toString(takeOutSmallest(arr2)));
    }

    public static int[] takeOutSmallest(int[] arr) {

        if (arr.length == 1) {
            int[] result = {-1};
            return result;
        }

        int smallest = arr[0];
        for (int i = 1; i < arr.length; i++) {
            smallest = Math.min(smallest, arr[i]);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != smallest) {
                result.add(arr[i]);
            }
        }
        int[] answer = new int[result.size()];
        // List<Integer> -> int[]
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}
