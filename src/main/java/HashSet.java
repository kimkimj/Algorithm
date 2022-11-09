/*
    포켓몬의 개수 / 2 한 수가 unique numbers 보다 작다면, 포캣몬개수를 return
    n/2 < unique numbers, return n/2
    n/2 >= unique numbers, return unique numbers


import java.util.*;

public class HashSet {

    public static void main(String[] args) {
        int[] nums = {3,1,2,3};
        System.out.println(solution(nums));
    }

    public static int solution(int[] nums) {
        //Set<Integer> set = new HashSet();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        int half = nums.length / 2;
        if (half < set.size()) {
            return half;
        } else {
            return set.size();
        }
    }
}

*/
