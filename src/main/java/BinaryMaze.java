import java.util.Arrays;

public class BinaryMaze {
    public static void main(String[] args) {
        int[] map1 = {9, 20, 28, 18, 11};
        int[] map2 = {30, 1, 21, 17, 28};
        int length = 5;
        String[] finalMap = solution(length, map1, map2);
        System.out.println(Arrays.toString(finalMap));
    }

    public static String[] solution(int n, int[] arr1, int[] arr2) {
        String[] result = new String[n];
        for (int i = 0; i < n ; i++) {
            result[i] = row(arr1[i], arr2[i], n);
        }
        return result;
    }

    public static String row(int map1, int map2, int length) {
        StringBuilder sb = new StringBuilder();
        int[] map1row = toBinary(map1, length);
        int[] map2row = toBinary(map2, length);
        for (int i = 0; i < length; i++) {
            if (map1row[i] == 1 || map2row[i] == 1) {
                sb.append("#");
            } else {
                sb.append(" ");
            }
        }
        return sb.toString();
    }

    public static int[] toBinary(int num, int length) {
        int[] result = new int[length];
        for (int i = length - 1; i >= 0; i--) {
            if (num >  0) {
                result[i] = (num % 2);
                num /= 2;
            }
        }
        return result;
    }
}
