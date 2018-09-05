public class Solution {
    public int UniquePaths(int m, int n) {
        int [,] mem = new int[m,n];
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i==0 || j==0) mem[i,j] = 1;
                else{
                    mem[i,j] = mem[i-1, j] + mem[i,j-1];
                }
            }
        }
        return mem[m-1,n-1];
    }
}