// 1 is not a prime number
// 2, 3, 5, 7 are prime numbers and should not be excluded by the staement if (n % (2, 3, 5, 7) == 0): pirimeNumber = false

public class PrimeNumber {
    public static void main(String[] args) {
        int n = 10;
        System.out.println("prime number: " + solution(n));
    }

    public static int solution(int n) {
        int count = 1;
        int[] divider = {2, 3, 5, 7};
        for (int i = 3; i <= n; i++) {
            boolean primeNumber = true;
            for (int j = 0; j < divider.length; j++) {
                if (i != divider[j] && i % divider[j] == 0) {
                    primeNumber = false;
                }
            }
            if (primeNumber) {
                count++;
            }
        }
        return count;
    }
}
