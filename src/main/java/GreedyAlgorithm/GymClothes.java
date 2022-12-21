package GreedyAlgorithm;

public class GymClothes {
    public static void main(String[] args) {
        int[] lost = {3};
        int[] reserve = {1, 3, 5};
        int[] reserve2 = {1};
        int n = 3;

        int answer = solution(n, lost, reserve2);
        System.out.println(answer);
    }

    public static int solution(int n, int[] lost, int[] reserve) {
        int count = n - lost.length;
        int[] students = new int[n];

        // mark students with extra clothes with 1
        for (int i = 0; i < reserve.length; i++) {
            int index = reserve[i] - 1;
            students[index] = 1;
        }

        // iterate through the students who don't have the clothes and check
        // if their front or back are marked with 1.
        for (int i = 0; i < lost.length; i++) {
            int index = lost[i] - 1;

            if (index - 1  >= 0 && students[index - 1] == 1) {
                count++;
            } else if (index + 1 < students.length && students[index + 1] == 1) {
                count++;
                students[index + 1] = 0;
            }
        }
        return count;
    }
}
