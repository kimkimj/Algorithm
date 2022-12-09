public class Recursion {
    public static void main(String[] args) {
        System.out.println(gcd(14, 28));

    }

    // codeup 2623 최대 공약수 찾기
    public static int gcd(int num1, int num2){
        if (num1 ==1 | num2 == 1) {
            return 1;
        }
        if (num1 == num2) {
            return num1;
        }
        return gcd(Math.max(num1, num2) - Math.min(num1, num2), Math.min(num1, num2));
    }

    // 1851  n개의 별 출력하기
    public static void stars(int num, int count) {
        if (count <= num) {
            System.out.print("*");
            stars(num, ++count);
        }
    }

    // 1912 n factorial 반환하기
    public static int factorial(int num) {
        if (num == 0) {
            return 1;
        }
        return num * factorial(num - 1);
    }

    public static int fibonacci(int num) {
        if (num == 0 || num == 1) {
            return num;
        }
        return fibonacci(num - 2) + fibonacci(num - 1);
    }
}
