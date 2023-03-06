package DP;

// Given the costs to get to the position in a 2-dimensional array
// this program finds the minimum cost to get the right corner
public class MinimumPath {
    public static void main(String[] args) {
        int[][] arr = {{1, 2}, {3, 4}};
        int[][] arr2 = {{1, 2, 1}, {3, 4, 1}, {1, 1, 1}};
        System.out.println(minCost(arr2));
    }

    public static int minCost(int[][] cost){
        int numRow = cost.length;
        int numCol = cost[0].length;

        // first row
        for (int i = 1; i < numCol; i++) {
            cost[0][i] += cost[0][i - 1];
        }

        // first column
        for (int i = 1; i < numRow; i++) {
            cost[i][0] += cost[i - 1][0];
        }

        // take the minimum value among the box above, across (left), and left to the current box
        for (int i = 1; i < numRow; i++) {
            for (int j = 1; j < numCol; j++) {
                int min = Math.min(cost[i - 1][j], cost[i - 1][j - 1]);
                min = Math.min(min, cost[i][j - 1]);
                cost[i][j] += min;
            }
        }
        return cost[numRow - 1][numCol - 1];
    }
}
