/*
    2차원 배열: 찍는 패턴을  각각의 배열에 저장
    pointer하나
    correct[]: 학생들의 맞힌 개수
    highest: 가장 높은 점수
    arraylist: 가장 높은 점수를 받은 학생

    for loop: 학생 수
        for loop: 질문 개수
            if answer[j] == patter[student(바깥 쪽 loop)][pointer]
                 correct[i]++;

    가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
        if correct[student] > highestScore
            update highestScore

    loop에 나와서 arraylist -> array
    return array
 */

import java.util.ArrayList;
import java.util.Arrays;

public class Programmers_MathStudents {
    public static void main(String[] args) {
        int[] answers = {1,2,3,4,5};
        int[] result = solution(answers);
        System.out.println(Arrays.toString(result));
    }
    public static int[] solution(int[] answers) {
        int[] answer = {};
        int[][] guessingPattern = {{1, 2, 3, 4, 5}, { 2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int[] correct = new int[3];
        int highestScore = 0;

        for (int student = 0; student < 3; student++) {
            int pointer = 0;
            for (int question = 0; question < answers.length; question++) {
                if (pointer == guessingPattern[student].length){
                    pointer = 0;
                }
                if(answer[question] == guessingPattern[student][pointer]){
                    correct[student]++;
                    if (correct[student] > highestScore){
                        highestScore = correct[student];
                    }
                }
            }
        }

        ArrayList<Integer> studentWithHighest = new ArrayList<>();
        for (int i = 0; i <3; i++) {
            if (correct[i] == highestScore){
                studentWithHighest.add(i);
            }
        }
        int[] result = studentWithHighest.stream().mapToInt(i -> i).toArray();
        return result;
    }

}


