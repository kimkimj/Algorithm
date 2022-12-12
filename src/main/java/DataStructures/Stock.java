package DataStructures;

import java.util.Arrays;

public class Stock {
    public static void main(String[] args) {
        int[] prices = {1, 2, 3, 2, 3};
        int[] answer = secondsUntilDrop(prices);
        System.out.println(Arrays.toString(answer));
    }

    public static int[] secondsUntilDrop(int[] prices) {
        int length = prices.length;
        int[] answer = new int[length];

        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {
                answer[i]++;
                if (prices[i] > prices[j]) {
                    break;
                }
            }
        }
        return answer;
    }
}
