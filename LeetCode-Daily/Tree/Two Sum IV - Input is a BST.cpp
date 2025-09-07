/*
@ Leetcode : 653. Two Sum IV - Input is a BST
@ description : Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
@ T.C : O(n)
@ S.C : O(n)
*/
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
    bool inorder(TreeNode *root,int k,unordered_map<int,int>&mp){
        if (root == nullptr){
            return false;
        }

        bool leftPart = inorder(root->left,k,mp);
        if (mp[k - root->val] > 0){
            return true;
        }
        mp[root->val] += 1;
        bool rightPart = inorder(root->right,k,mp);
        return leftPart || rightPart;
    }
public:
    bool findTarget(TreeNode* root, int k) {
        unordered_map<int,int>mp;
        return inorder(root,k,mp);
    }
};