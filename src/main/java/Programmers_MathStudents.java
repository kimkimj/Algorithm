import java.util.ArrayList;
import java.util.Arrays;

public class Programmers_MathStudents {
    public static void main(String[] args) {
        int[] answers = {1,2,3,4,5};
        int[] result = solution(answers);
        System.out.println(Arrays.toString(result));
    }
    public static int[] solution(int[] answers) {
        // 2차원 배열: [학생번후][찍는 패턴]
        int[][] guessingPattern = {{1, 2, 3, 4, 5}, { 2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};

        // 학생 당 맞은 개수
        int[] correct = new int[3];
        int highestScore = 0;

        // 학생 한명씩 iterate
        for (int student = 0; student < 3; student++) {
            // 찍기 패턴을 pointer로 관리
            int pointer = 0;

            // 정답 하나씩 iterate
            for (int question = 0; question < answers.length; question++) {

                // pointer가 마지막 패턴에 있으면 다시 처음으로
                if (pointer == guessingPattern[student].length){
                    pointer = 0;
                }

                // 찍은 번호가 정답이면 학생의 맞은 개수에 추가
                if(answers[question] == guessingPattern[student][pointer]){
                    correct[student]++;

                    // 만약 맞은 개수가 현재 가장 높은 점수보다 높으면 가장 높은 점수로 저장
                    if (correct[student] > highestScore){
                        highestScore = correct[student];
                    }
                }
                pointer++;
            }
        }

        // arraylist: 가장 높은 점수를 받은 학생
        ArrayList<Integer> studentWithHighest = new ArrayList<>();

        // 학생의 맞은 개수를 저장한 배열을 iterate하며 가장 높은 점수와 같다면 arraylist에 추가한다
        for (int i = 0; i <3; i++) {
            if (correct[i] == highestScore){
                studentWithHighest.add(i + 1);
            }
        }

        // arraylist를 int 배열로 바꾼다
        int[] result = studentWithHighest.stream().mapToInt(i -> i).toArray();
        return result;
    }

}


