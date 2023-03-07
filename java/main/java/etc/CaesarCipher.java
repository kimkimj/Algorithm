package etc;

public class CaesarCipher {

    public static void main(String[] args) {
        System.out.println(solution("ABc", 1));
        System.out.println(solution("z", 1));
        System.out.println(solution("a B z", 4));
    }

    public static String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            boolean lowerCase = false;
            if (letter >= 'a' && letter <= 'z') {
                lowerCase = true;
            }
            if (letter != ' ') {
                letter += n;
                if (!lowerCase && letter > 'Z' || lowerCase && letter > 'z')  {
                    letter -= 26;
                }
            }
            sb.append(letter);
        }
        return sb.toString();
    }
}

