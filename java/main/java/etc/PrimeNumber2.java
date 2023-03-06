package etc;

import java.util.ArrayList;
import java.util.List;

/*
   * 에라토스테네의 체: 2, 3, 5, 7의 배수를 array에서 한 배수씩 지우준다. 남은 수가 prime number이다
   * Create an array of booleans with size up to n
   * If the number is a multiple of  dptm
   *
   * 배열을 통채로 쯔는 게 arraylist에서 add, remove하는 것보다 훨씬 빠르다.
   * ArrayList에 remove를 하면 복사를 해야 하기때문에 O(n)
 */
public class PrimeNumber2 {
    public static void main(String[] args) {
        //int answer = solution(10);
        //ystem.out.println(answer);
    }

    /*
    public static int solution(int num){
        int count = 1;
        int[] numbers = new int[num - 1];
        // int로 casting을 해줘야 한다
        int root = (int) Math.sqrt(num);
        for (int i = 2; i <= root ; i++) {
            for (int j = i; i * j <= num; j++) {
                numbers[i * j] = 1;
            }
        }
        for (int i = 3; i < num; i++) {
            if (numbers[i] == 0){
                count++;
            }
        }
        return count;
    }*/
}

