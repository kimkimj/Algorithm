package DataStructures;

import java.util.*;

public class PrintQueue {
    public static void main(String[] args) {
        int[] arr1 = {2, 1, 3, 2};
        System.out.println(numberInLine(arr1, 2));

        int[] arr2 = {1, 1, 9, 1, 1, 1};
        System.out.println(numberInLine(arr2, 0));

    }

    public static int numberInLine(int[] priorities, int location) {
        // 아직 프린트 되지 않은 문서들의 index를 담는 queue
        Queue<Integer> queue = new LinkedList<>();

        // 문서의 index를 프린트 순서로 장하는 list
        List<Integer> sorted = new ArrayList<>();

        // 문서의 index를 우선순위를 기준으로 내림차순으로 저장하는 pq
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        // 각 문서들의 우선순위가 담겨있는 배열을 queue와 pq에 더한다
        for (int i = 0; i < priorities.length; i++) {
            queue.add(i);
            pq.add(priorities[i]);
        }

        // queue에 아무것도 없을 때까지 반복
        while(!queue.isEmpty()) {

            // queue에서 가장 앞에 있는 문서를 꺼내 우선순위를 확인한다
            int index = queue.remove();
            int current = priorities[index];

            // 문서의 우선순위가 pq의 가장 윗 수 (가장 높은 우선 순위)와 일치한다면
            if (current == pq.peek()) {
                // sorted에 index를 더하고 pq에서 뺀다
                sorted.add(index);
                pq.poll();

            } else {
                // pq의 가장 위에 있는 수와 일치하지 않는다면 더 높은 우선순위의 수가 있으므로
                // queue에 다시 더한다
                queue.add(index);
            }
        }

        // find the given value in the array
        // 줄 가장 앞에 있는 것을 0이 아니라 1로 세기 때문에 1을 더해준다
        return sorted.indexOf(location) + 1;
    }

    // 다른 방법
    public int solution(int[] priorities, int location) {

        int number = 1;

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i : priorities) {
            pq.add(i);
        }

        while (!pq.isEmpty()) {

            for (int i = 0; i < priorities.length; i++) {

                if (pq.peek() == priorities[i]) {
                    if (location == i) {
                        return number;
                    }
                    pq.poll();
                    number++;
                }
            }
        }
        return number;
    }
}
