/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public bool IsValidBST(TreeNode root) {
        return Helper(root, -1, -1);
    }
    
    private bool Helper(TreeNode root, int min, int max){
        if(root == null) return true;
        if(root.left == null || (root.left.val < root.val && (min == -1 || root.left.val > min))){
            if(Helper(root.left, min, root.val)){
                if(root.right == null || (root.right.val > root.val &&(max == -1 || root.right.val < max))){
                    return Helper(root.right, root.val, max); 
                }
            }
        }
        return false;
    }
}