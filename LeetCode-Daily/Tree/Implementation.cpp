#include<bits/stdc++.h>
using namespace std;
class TreeNode{
public:
	int data;
	TreeNode *left;
	TreeNode *right;
	
	TreeNode(int val){
		this->data = val;
		this->left = NULL;
		this->right = NULL;
	}
};

TreeNode *insertNode(TreeNode *root,int val){
	if (root == nullptr){
		// Assign a new node of the tree
		TreeNode *root = new TreeNode(val);
		return root;
	}
}

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	TreeNode *root = new TreeNode(20);
	cout<<root->data<<endl;
}
