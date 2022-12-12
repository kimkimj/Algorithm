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
        Queue<Integer> queue = new LinkedList<>();
        ArrayList<Integer> sorted = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < priorities.length; i++) {
            queue.add(i);
            pq.add(priorities[i]);
        }
        while(!queue.isEmpty()) {
            int index = queue.remove();
            int current = priorities[index];
            if (current == pq.peek()) {
                sorted.add(index);
                pq.poll();
            } else {
                queue.add(index);
            }
        }

        // find the given value in the array
        // 줄 가장 앞에 있는 것을 0이 아니라 1로 세기 때문에 1을 더해준다
        return sorted.indexOf(location) + 1;
    }
}
