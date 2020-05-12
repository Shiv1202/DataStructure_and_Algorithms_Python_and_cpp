/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int parent(TreeNode* node,int n)
    {
        if(node==NULL) 
            return -1;
        else 
            if((node->left!=NULL && node->left->val==n) || (node->right!=NULL && node->right->val==n)) 
                return node->val;
             else
                return max(parent(node->left,n),parent(node->right,n));
    }
    int level(TreeNode* node, int n, int d)
    {
        if(node==NULL) 
            return 0;
        else if(node->val==n)
            return d;
        else 
            return max(level(node->left,n,d+1),level(node->right,n,d+1));
    }
    
    bool isCousins(TreeNode* root, int x, int y) {
        int levelx= level(root,x,0);
        int levely= level(root,y,0);
        if(levelx!=levely)
            return false;
        
        if(parent(root,x)==parent(root,y))
            return false;
        else
            return true;
    }
};
