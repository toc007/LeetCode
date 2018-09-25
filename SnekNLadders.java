import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    int N;
    HashMap<Integer, Integer> SnekNLadderMap;
    PriorityQueue<Integer> SnekNLadders;
    private int numberToValue(int[][] board, int number) {
        // for 0-indexing
        number--;
        int row = N-(number/N)-1;
        int col = number%N;
        if (N%2 == 0) {
            if (row % 2 == 0) {
                col = N-col-1;
            }
        }
        else {
            if (row % 2 != 0) {
                col = N-col-1;
            }
        }
        return board[row][col];
    }
    public int snakesAndLadders(int[][] board) {
        N = board.length;
        for (int i=1; i<=N*N; i++) {
            int valAtI = numberToValue(board, i);
            if (valAtI != -1) {
                SnekNLadderMap.put(i, valAtI);
                SnekNLadders.add(i);
            }
        }
        return -1;
    }
}