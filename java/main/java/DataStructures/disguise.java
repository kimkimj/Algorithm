package DataStructures;

import java.util.HashMap;
import java.util.Map;

public class disguise {

    public static void main(String[] args) {

        String[][] arr = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        System.out.println(solution(arr));

        String[][] arr1 = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
        System.out.println(solution(arr1));

    }

    public static int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < clothes.length ; i++) {
            String type = clothes[i][1];
            if (!map.containsKey(type)) {
                map.put(type, 1);
            } else {
                map.put(type, map.get(type) + 1);
            }

        }
        int answer = 1;
        for (int size: map.values()) {
            answer *= (size + 1);
        }
        return answer - 1;
    }
}
