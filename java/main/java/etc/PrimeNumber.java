package etc;// 1 is not a prime number
// 2, 3, 5, 7 are prime numbers and should not be excluded by the staement if (n % (2, 3, 5, 7) == 0): pirimeNumber = false

import java.util.Arrays;

public class PrimeNumber {

        // 2랑 3일때 틀림.
    public static void main(String[] args) {
        int n = 100;
        int sol2 = solution2(3);
        System.out.println(sol2);
        //System.out.println("prime number: " + solution(n));
    }

    public static int solution2(int n){
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        for (int i = 4; i <= n; i+= 2) {
            isPrime[i] = false;
        }
        int count = 0;
        for (int i = 0; i < isPrime.length; i++) {
            if (isPrime[i]){
                count++;
            }
        }
        return count;
    }

    public static int solution(int n) {
        int count = 1;
        int[] divider = {2, 3, 5, 7};
        for (int i = 3; i <= n; i++) {
            boolean isPrime = true;
            for (int j = 0; j < divider.length; j++) {
                if (i != divider[j] && i % divider[j] == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                count++;
            }
        }
        return count;
    }
}
