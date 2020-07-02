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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if(root==NULL)
            return res;
        
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            int qlen=q.size();
            vector<int> nodes;
            for(int i=0;i<qlen;i++)
            {
                root=q.front();
                q.pop();
                nodes.push_back(root->val);
                if(root->left!=NULL)
                    q.push(root->left);
                if(root->right!=NULL)
                    q.push(root->right);
            }
            res.push_back(nodes);
        }  
        return { res.rbegin(),res.rend() };
    }
};
