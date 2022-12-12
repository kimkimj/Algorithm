package DP;

import java.util.Arrays;

public class Stock {
    public static void main(String[] args) {
        int[] prices = {1, 2, 3, 2, 3};
        int[] answer = secondsUntilDrop(prices);
        System.out.println(Arrays.toString(answer));
    }

    public static int[] secondsUntilDrop(int[] prices) {

        int[] answer = new int[prices.length];
        for (int i = 0; i < answer.length - 1; i++) {
            int count = 0;
            for (int j = i + 1; j < answer.length; j++) {
                count++;
                if (prices[j] < prices[i]) {
                    break;
                }
            }
            answer[i] = count;
        }
        return answer;
    }
}
