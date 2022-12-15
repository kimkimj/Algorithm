package Sort;

import java.util.Arrays;

public class BiggestNumber {
    public static void main(String[] args) {
        
    }

    // O(n!) 모든 경우의 수를 만들면

    // 가장 큰 자릿수부터 비교?
    /*
    Use a linked list
    if the current number's first digit > root,
    make it the root
    else if <:
    else if =: compare the second digit (if one number does not have the digit,
        eg. 3 vs. 31, if
        eg. e vs. 30: if the seocnd digit is zero, the smaller number is taken

     */
    public static String biggestNumber(int[] arr) {
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {

        }
    }
}
