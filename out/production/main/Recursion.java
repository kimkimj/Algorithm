public class Recursion {
    public static void main(String[] args) {
        printTo100(1);
    }

    public static void printTo100(int num) {
        if (num < 101) {
            System.out.print(num);
            printTo100(++num);
        }
    }

}
