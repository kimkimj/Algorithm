package etc;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

// 처음에는 set을 이용해 풀었지만 문제를 자세히 보니 바로 앞에 나오는 수가 아니면 중복된 숫자로 치지 않는다

public class DuplicateNumbersInArray {
    public static void main(String[] args) {
        int[] arr1 = {1,1,3,3,0,1,1};
        int[] arr2 = {4,4,4,3,3};
        arr1 = solution(arr1);
        arr2 = solution(arr2);
        System.out.println(Arrays.toString(arr1));
        System.out.println(Arrays.toString(arr2));

    }

    public static int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        int prev = -1;
        for (int i = 0; i < arr.length ; i++) {
            if (arr[i] != prev) {
                list.add(arr[i]);
            }
            prev = arr[i];
        }
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size() ; i++) {
            result[i] = list.get(i);
        }
        return result;
    }

}
