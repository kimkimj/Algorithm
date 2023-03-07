package DP;

public class LCS {
    public static void main(String[] args) {
        String s1 = "AAAEEDD";
        String s2 = "AAAZDD";

        System.out.println(lcs(s1, s2));
    }

    // DP를 이용한 DP.LCS
    // 어느쪽이 더 길어도 상관이 없다
    public static String lcs(String s1, String s2) {
        int[][] memo = new int[s1.length() + 1][s2.length() + 1];
        // to get the number of rows of a two-dimensional array: arr.length
        // to get the number of columns of a two-dimensional array: arr[].length

        // 철 행과 열은 0이여야 하기 때문에 1열, 1행에서 시작한다
        for (int i = 1; i < memo.length; i++) {

            // 열이나 행 중 하나를 정해서 letter를 비교한다
            // int[row][column]
            // row
            char rowLetter = s1.charAt(i - 1);

            // column
            for (int j = 1; j < memo[0].length; j++) {
                char colLetter = s2.charAt(j - 1);

                // 비교하는 글자들이 같으면 대각선에서 1를 더한 값을 저장
                if (rowLetter == colLetter){
                    memo[i][j] = memo[i - 1][j - 1] + 1;

                // 다르다면 바로 위나 옆의 칸 중에서 더 큰 값을 저장
                } else {
                    memo[i][j] = Math.max(memo[i][j - 1], memo[i - 1][j]);
                }
            }
        }

        // 마지막 칸에 있는 수가 lcs수이다
        int lastRow = memo.length - 1;
        int lastCol = memo[0].length - 1;
        int count = memo[lastRow][lastCol];

        // LCS를 반환
        StringBuilder sb = new StringBuilder();

        // 마지막 칸에서 시작한다
        int currentRow = lastRow;
        int currentCol = lastCol;

        // StringBuilder의 길이가 위에서 구한 lcs 수와 같아질 때까지 while loop를 돌린다
        while(sb.length() < count) {

            // 현재 칸의 값과 윗칸의 값이 같으면 윗칸으로 이동
            if (memo[currentRow][currentCol] == memo[currentRow - 1][currentCol]) {
                currentRow--;

            // 현재 칸의 갑이 옆칸의 값과 같다면 옆칸으로 이동
            } else if (memo[currentRow][currentCol] == memo[currentRow][currentCol - 1]) {
                currentCol--;

            // 윗칸과 옆칸이 현재 칸의 값과 같지 않다면 대각선으로 이동하고 현재 값을 StringBuilder에 더한다
            } else {
                sb.append(s1.charAt(currentRow - 1));
                currentRow--;
                currentCol--;
            }
        }

        // 맨 아랫칸 (가장 끝 letter)에서 시작했으므로 StrinbBuilder를 reverse하고 String으로 변환해서 반환
        return sb.reverse().toString();
    }
}
