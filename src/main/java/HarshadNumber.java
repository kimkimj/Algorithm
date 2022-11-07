public class HarshadNumber {
    public static void main(String[] args) {
        System.out.println(solution(13));
    }

    public static boolean solution(int num){
        /*
            temp로 숫자를 복사
            temp % 10 으로 마지막자리수를 구한다
            숫자의 자릿수를 구한다: int값을 /10 으로 나눈다 until 값이 0이 나올 때까지 (3 / 10 = 0)
            나눈 값을 계속 sum에 더해준다
            num % sum == 0
         */
        int temp = num;
        int sum = 0;
        do {
            sum += temp % 10;
            temp /= 10;
        } while (temp != 0);

        return num % sum == 0;
    }

}
