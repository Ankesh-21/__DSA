/*
* LeetCode : 45
* T.C : o(N * K) Where K is maximum element of the array
* S.C : O(N)
*/

// Recursive and Memoize solution (Accepted)
class Solution {
    long long int solve(vector<int>&nums,int ind,int cnt,vector<int>&dp){
        if (ind >= nums.size()){
            return INT_MAX/2;
        }
        if (ind == nums.size()-1){
            return 0;
        }

        if (dp[ind]!= -1){
            return dp[ind];
        }

        long long int mini = INT_MAX;
        
        for (int j = 1;j<=nums[ind] && (ind + j) < nums.size();j++){
            mini = min(mini,1 + solve(nums,ind + j,cnt+1,dp));
        }

        return dp[ind]=mini;
    }
public:
    int jump(vector<int>& nums) {
        vector<int>dp(nums.size()+1,-1);
        return solve(nums,0,0,dp);
    }
};

// Greedy solution
/*
* T.C : O(N)
* S.C : O(1)
*/
class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        int curr = 0;
        int farthest = 0;

        for (int i = 0;i<nums.size()-1;i++){
            farthest = max(farthest , i + nums[i]);
            if (curr == i){
                jumps += 1;
                curr = farthest ;
            }
        }
        return jumps;
    }
};