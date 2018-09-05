public class Solution {
    public bool Exist(char[,] board, string word) {
        if(board == null || board.GetLength(0) == 0 || board.GetLength(1) == 0) return false;
        if(string.IsNullOrEmpty(word)) return true;
        for(int i=0; i < board.GetLength(0); i++){
            for(int j=0; j < board.GetLength(1); j++){
                if(Exist(board, word, i, j, 0, new bool [board.GetLength(0),board.GetLength(1)])) return true;
            }
        }
        return false;
    }
    
    private bool Exist(char[,] board, string word, int x, int y, int n, bool[,] traversed){
        if(n == word.Length) return true;
        if(x >= board.GetLength(0) || y >= board.GetLength(1) || x < 0 || y < 0 ||traversed[x,y]){
            return false;
        }
        if(board[x,y] == word[n]){
            traversed[x,y] = true;
            if(Exist(board, word, x-1,y,n+1,traversed) ||Exist(board,word,x+1,y,n+1,traversed) || Exist(board,word,x,y-1,n+1,traversed) ||                 Exist(board,word,x,y+1,n+1, traversed) ) return true;
            traversed[x,y] = false;
        }

        return false;
    }
}