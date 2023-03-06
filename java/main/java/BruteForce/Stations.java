package BruteForce;
import java.util.LinkedList;
import java.util.Queue;

// INCOMPLETE: Fails multiple tests & efficiency tests
public class Stations {
    public static void main(String[] args) {
        int[] stations = {4, 11};
        int answer = numStations(11, stations, 1);
        System.out.println(answer);

        int[] stations2 = {9};
        answer = numStations(16, stations2, 2);
        System.out.println(answer);
    }

    public static int numStations(int n, int[] stations, int w) {
        int[] arr = new int[n];
        int max = w * 2 + 1;
        int count = 0;
        // arr은 0에서 시작하고 stations는 1에서 시작한다는 것을 고려해야 한다
        Queue<Integer> lows = new LinkedList<>();
        Queue<Integer> highs = new LinkedList<>();
        for (int i = 0; i < stations.length; i++) {
            lows.add(stations[i] - w - 1);
            highs.add(stations[i] + w - 1);
            count += highs.peek() - lows.peek() + 1;
        }

        int newStations = 0;
        int current = 0; // 0이면 처음에 range계산할떼 오류

        while (count < n) {
            if (lows.isEmpty()){
                lows.add(n);
            }
            int numHouses = lows.remove() - current;
            count += numHouses;
            newStations += numHouses / max;
            if (numHouses % max != 0) {
                newStations++;
            }
            if (highs.isEmpty()) {
                current = n;
            } else {
                current = highs.remove() + 1;
            }
        }
        return newStations;
    }
}

