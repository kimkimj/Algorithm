package DataStructures;

// 프로그래머스 고득점 kit 다리를 지나는 트럭
public class Trucks {
    public static void main(String[] args) {


        int[] truck_weights = {7,4,5,6};
        int answer = solution(2,10, truck_weights);
        System.out.println(answer);

        int[] arr3 = {10};
        int answer3 = solution(100, 100, arr3);
        System.out.println(answer3);

        int[] arr2 = {10,10,10,10,10,10,10,10,10,10};
        int answer2 = solution(100, 100, arr2);
        System.out.println(answer2);

        int[] arr4 = {2, 2, 2, 2, 1, 1, 1, 1, 1};
        System.out.println(solution(5, 5, arr4));
    }

    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int backPointer = 0;
        int frontPointer = 0;
        int num_trucks_on_road = 1;
        int currentWeight = truck_weights[0];
        int time = 1;
        int[] timeElapsed = new int[truck_weights.length];
        timeElapsed[0]++;

        while (frontPointer < truck_weights.length && backPointer < truck_weights.length) {

            // 1 second passes
            time++;

            // 다리를 건너는 중인 모든 트럭의 머물고 있는 시간을 올려준다
            for (int i = frontPointer; i <= backPointer; i++) {
                if (timeElapsed[i] < bridge_length) { // if the truck is still crossing the bridge
                    timeElapsed[i]++;

                } else { // a truck has crossed the bridge and another truck can be checked for boarding the bridge
                    currentWeight -= truck_weights[frontPointer];
                    frontPointer++;
                    num_trucks_on_road--;
                }
            }

            // check if another truck can go on the road
            // is the current backPointer at the end of the array and will adding 1 to the backpointer cause a null pointer exception?
            // will adding another truck exceed the weight limit?
            if (backPointer + 1 < truck_weights.length &&
                    num_trucks_on_road < bridge_length) {
                if (currentWeight + truck_weights[backPointer + 1] <= weight) {
                    backPointer++;
                    currentWeight += truck_weights[backPointer];
                    timeElapsed[backPointer]++;
                    num_trucks_on_road++;
                }
            }
        }
        return time;
    }
}
