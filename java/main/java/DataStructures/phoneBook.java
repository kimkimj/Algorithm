package DataStructures;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

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

        Set<String> set = new HashSet<>();

        for (int i = 0; i < phone_book.length; i++) {
            set.add(phone_book[i]);
        }

        for (String number: set) {
            for (int i = 0; i < number.length(); i++) {
                if (set.contains(number.substring(0, i))) {
                    return false;
                }
            }
        }
        return true;
    }
}
