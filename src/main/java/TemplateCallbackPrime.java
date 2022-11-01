class TemplateCallbackPrime {
    boolean isBbigger(int a, int b) {
        return a < b;
    }

    boolean isPrime(int num) {
        for (int i = 2; isBbigger(i, num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        TemplateCallbackPrime tcp = new TemplateCallbackPrime();
        boolean r = tcp.isPrime(17);
        System.out.println(r);

    }
}
