package GreedyAlgorithm;

public class GymClothes {
    public static void main(String[] args) {
        int[] lost = {2, 4};
        int[] reserve = {1, 3, 5};

        int answer = solution(5, lost, reserve);
        System.out.println(answer);
    }

    public static int solution(int n, int[] lost, int[] reserve) {
        int count = n - lost.length;
        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if (lost[i] == reserve[j] + 1) {
                    count++;
                }
            }
        }
        return count;
    }
}
