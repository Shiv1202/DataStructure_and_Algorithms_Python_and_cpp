/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructBinTree(TreeNode *root, int &cval) {
        if(root==NULL) {
            root=new TreeNode(cval);
            
        } else if(cval < root->val) {
            root->left = constructBinTree(root->left, cval);
        } else if( cval> root->val) {
            root->right = constructBinTree(root->right, cval);
        }
        return root;
        
    }
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode *root = constructBinTree(root,preorder[0]);
        for(int i = 1; i<preorder.size() ;i++) {
            constructBinTree(root,preorder[i]);
        }
        return root;
    }
    
};
