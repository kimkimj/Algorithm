package DataStructures;

import java.util.Arrays;
import java.util.Comparator;

public class phoneBook {
    public static void main(String[] args) {
        String[] arr = {"119", "97674223", "1195524421"};
        System.out.println(solution(arr));

        String[] arr1 = {"123","456","789"};
        System.out.println(solution(arr1));

        String[] arr2 = {"12","123","1235","567","88"};
        System.out.println(solution(arr2));
    }

    public static boolean solution(String[] phone_book) {
        if (phone_book.length == 1) {
            return true;
        }
        Arrays.sort(phone_book, Comparator.comparingInt(String::length));
        for (int i = 0; i <phone_book.length -1; i++) {
            for (int j = i + 1; j < phone_book.length; j++) {
                if (phone_book[j].indexOf(phone_book[i]) != -1) {
                    return false;
                }
            }
        }
        return true;
    }
}
