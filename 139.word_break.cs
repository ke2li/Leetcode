public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        //return Helper(s, 0, wordDict);
        return Helper(s, wordDict);
    }
    
    /*private bool Helper(string s, int end, IList<string> wordDict){
        int start = 0;
        for(int i = end; i < s.Length; i++){
            if(wordDict.Contains(s.Substring(start, i-start + 1))){
                start = i+1;
                if(start == s.Length) return true;
                if(Helper(s, start, wordDict)) return true;
            }
        }
        return false;
    }*/
    
    /*private bool Helper(string s, IList<string> wordDict){
        for(int i = 0; i <s.Length; i++){
            if(wordDict.Contains(s.Substring(0,i+1))){
                if(i+1 == s.Length) return true;
                if(Helper(s.Substring(i+1), wordDict)) return true;
            }
        }
        return false;
    }*/
    
    private bool Helper(string s, IList<string> wordDict){
        bool[] x = new bool[s.Length+1];
        x[0] = true;
        for(int i = 1; i <= s.Length; i++){
            for(int j = 0; j < i; j++){
                if(x[j] && wordDict.Contains(s.Substring(j,i-j))){
                    x[i] = true;
                    break;
                }
            }
        }
        return x[s.Length];
    }
}