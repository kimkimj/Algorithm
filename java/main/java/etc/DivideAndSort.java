package etc;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.FormatterClosedException;
import java.util.PriorityQueue;

public class DivideAndSort {
    public static void main(String[] args) {
        int[] arr = {5, 9, 7, 10};
        int[] result = solution(arr, 5);
        System.out.println(Arrays.toString(result));
    }

    public static int[] solution(int[] arr, int divisor) {
        /*
            arraylist를 만든다
            for each로 숫자를 하나씩 꺼내 number % divisor == 0 면 숫자를 result에 추가, size도 +1
            arraylist가 비어있다면 return int[] result = {-1};
            아니라면, arraylist를 int로 바꾸어 준다
                SORT 를 해야한다

         */
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int num: arr) {
            if (num % divisor == 0){
                numbers.add(num);
            }
        }
        if (numbers.isEmpty()){
            int[] result = {-1};
            return result;
        } else{
            int[] result = new int[numbers.size()];
            for (int i = 0; i < numbers.size() ; i++) {
                //result[i] = numbers.get(i).intValue();
                result[i] = numbers.get(i);
            }
            Arrays.sort(result);
            return result;
        }
    }

    public static int[] solution2(int[] arr, int divisor){
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num: arr) {
            if (num % divisor == 0){
                pq.add(num);
            }
        }
        if (pq.isEmpty()){
            int[] result = {-1};
            return result;
        } else{
            int[] result = new int[pq.size()];
            int index = 0;
            while (!pq.isEmpty()){
                result[index++] = pq.poll();
            }
            return result;
        }
    }
}
