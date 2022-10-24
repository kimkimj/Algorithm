import java.util.Arrays;
import java.util.PriorityQueue;

public class SortingArray {
    public int[] solution(int[] array, int[][] commands) {
        public int getKthNum ( int[] command){
            int frIdx = command[0]; // 0번 from
            int toIdx = command[1]; // 1번 to
            int nth = command[2]; // n번째

            int result = 0; // 문제에 0이 안나온다고 했기 때문에 3벌식
            PriorityQueue<Integer> pq = new PriorityQueue<>();
            for (int i = frIdx - 1; i < toIdx; i++) { // 1번부터 시작하니 -1
                pq.add(arr[i]);
            }

            for (int i = 0; i < nth; i++) {
                result = pq.poll(); // stack의 pop과 비슷
            }
            return result;
        }

        public int[] solution ( int[] arr, int[][] commands){
            this.arr = arr;
            int[] answer = new int[commands.length];
            for (int i = 0; i < commands.length; i++) {
                answer[i] = getKthNum(commands[i]);
            }
            return answer;
        }
    }
}
