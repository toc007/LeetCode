import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.HashSet;

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
    
    private int bfs() {
        HashSet<Integer> Neighbors = new HashSet<>();
        HashSet<Integer> Working = new HashSet<>();
        HashSet<Integer> Seen = new HashSet<>();
        int depth = 0;
        Neighbors.add(1);
        while(Neighbors.size() > 0) {
            // copy everything from neighbors to the working set
            Working = new HashSet(Neighbors);
            // clear out the neighbors to add in the next layer
            Neighbors.clear();
            for(Integer node:Working) {
                // if goal is reached return the depth
                if(node >= N*N) { 
                    return depth;
                }

                // add neighbors of node to Neighbors
                for(int i=1; i<=6; i++) {
                    int neighborNode = node+i;
                    // make translation if neighbor is a snake/ladder
                    if(SnekNLadderMap.containsKey(neighborNode)) {
                        neighborNode = SnekNLadderMap.get(neighborNode);
                    }

                    // if the neighboring node has not been visited, add to
                    //  the Neighbors set to be visited next iteration
                    if(!Seen.contains(neighborNode)) {
                        Neighbors.add(neighborNode);
                    }
                }

                // add node to Seen
                Seen.add(node);
            }

            depth++;
        }
        return -1;
    }
    
    public int snakesAndLadders(int[][] board) {
        N = board.length;
        SnekNLadderMap = new HashMap<Integer, Integer>();
        for (int i=1; i<=N*N; i++) {
            int valAtI = numberToValue(board, i);
            if (valAtI != -1) {
                SnekNLadderMap.put(i, valAtI);
            }
        }
        
        return bfs();
    }
}