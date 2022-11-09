import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = {2, 7, 4, 9, 10, 223, 111, 23, 3, 39};
        System.out.println(Arrays.toString(ascending(arr)));
        System.out.println(Arrays.toString(descending(arr)));
    }
    
    public static int[] ascending(int[] arr) {

        for (int i = 0; i < arr.length - 1; i++) {
            int min = arr[i];
            int minIndex = i;
            for (int j = i; j < arr.length; j++) {
                if (arr[j] < min) {
                    min = arr[j];
                    minIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = min;
            arr[minIndex] = temp;
        }
        return arr;
    }

    public static int[] descending(int[] arr) {

        for (int i = 0; i < arr.length - 1; i++) {
            int max = arr[i];
            int maxIndex = i;
            for (int j = i; j < arr.length; j++) {
                if (arr[j] > max) {
                    max = arr[j];
                    maxIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = max;
            arr[maxIndex] = temp;
        }
        return arr;

    }
    
}
