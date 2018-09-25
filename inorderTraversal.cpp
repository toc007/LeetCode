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
    vector<int> inorderTraversal(TreeNode* root) {

        vector<int> res;
        stack<TreeNode*> pending;
        unordered_set<TreeNode*> seen;
        
        if (!root){
            return res;
        }
        
        pending.push(root);
        while(!pending.empty()) {
            TreeNode* working = pending.top();
            pending.pop();
            //cout << working->val << endl;

            // working->left exists
            if(working->left) {
                //cout << "left node" << endl;
                //cout << "seen size: " << seen.size() << endl;
                //cout << seen.count(working) << endl;
                if (seen.count(working)) {
                    res.push_back(working->val);
                    if (working->right) {
                        pending.push(working->right);
                    }
                }
                else {
                    // push all left nodes into stack
                    seen.insert(working);
                    pending.push(working);
                    pending.push(working->left);
                }                    
            }
            // working->right exists, and no left
            else if(working->right) {
                res.push_back(working->val);
                pending.push(working->right);
            }
            // no left and right children
            else {
                res.push_back(working->val);
            }
        }
        return res;
    }
};