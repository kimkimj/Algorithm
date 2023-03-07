package etc;

import java.sql.SQLOutput;
import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int days = sc.nextInt();

        int greatest = sc.nextInt();
        int sum = greatest;
        int maxDays = 1;
        for (int i = 0; i < num - 1; i++) {
            int nextNum = sc.nextInt();
            if (nextNum + sum > greatest) {
                greatest = nextNum + sum;
                maxDays++;
            }
        }
    }
}
