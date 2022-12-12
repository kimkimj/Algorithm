package DataStructures;

import java.util.Arrays;

public class Stock {
    public static void main(String[] args) {
        int[] prices = {1, 2, 3, 2, 3};
        int[] answer = secondsUntilDrop(prices);
        System.out.println(Arrays.toString(answer));
    }
    // 내 코드
    public int[] solution(int[] prices) {
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

    // 더 깔끔한 코드
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
