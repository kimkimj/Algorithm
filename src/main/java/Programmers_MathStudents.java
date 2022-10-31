// changed: pointer update와 필요없는데 있어서 answers배열과 혼동

import java.util.ArrayList;
import java.util.Arrays;

public class Programmers_MathStudents {
    public static void main(String[] args) {
        int[] answers = {1,2,3,4,5};
        int[] result = solution(answers);
        System.out.println(Arrays.toString(result));
    }
    public static int[] solution(int[] answers) {
        int[][] guessingPattern = {{1, 2, 3, 4, 5}, { 2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int[] correct = new int[3];
        int highestScore = 0;

        for (int student = 0; student < 3; student++) {
            int pointer = 0;
            for (int question = 0; question < answers.length; question++) {
                if (pointer == guessingPattern[student].length){
                    pointer = 0;
                }
                if(answers[question] == guessingPattern[student][pointer]){
                    correct[student]++;
                    if (correct[student] > highestScore){
                        highestScore = correct[student];
                    }
                }
                pointer++;
            }
        }

        ArrayList<Integer> studentWithHighest = new ArrayList<>();
        for (int i = 0; i <3; i++) {
            if (correct[i] == highestScore){
                studentWithHighest.add(i + 1);
            }
        }
        int[] result = studentWithHighest.stream().mapToInt(i -> i).toArray();
        return result;
    }

}


