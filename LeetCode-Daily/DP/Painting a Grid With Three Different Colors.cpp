/*
* LeetCode - 1931
* Hard
* Approach (Recursion + Memoization)
* T.C : O(n * S * S * m), where S = total states i.e. 3 * 2^m-1
* S.C : O((n * S) + (S * m)) where n * S is because of memoization array t, and S * m is for storing columnStates
*/

string s = "RGB";
int mod = 1e9 + 7;
class Solution {
    int get_mod(int a,int b){
        return ((a % mod) + (b % mod))% mod;
    }
    void col_states(string&temp,vector<string>&cols,int n){
        if (temp.size()==n){
            cols.push_back(temp);
            return;
        }
        for (int i=0;i<s.size();i++){
            if (temp.size() == 0 || temp.back()!=s[i]){
                temp.push_back(s[i]);
                col_states(temp,cols,n);
                temp.pop_back();
            }
        }
        return;
    }
    int solve(vector<string>&cols,int prev,int n,vector<vector<int>>&dp){
        if (n == 0){
            return 1;
        }
        if (dp[prev][n] != -1){
            return dp[prev][n];
        }
        int ans = 0;
        for (int i = 0;i<cols.size();i++){
            bool valid = true;
            for (int j = 0;j<cols[i].size();j++){
                if (cols[i][j] == cols[prev][j]){
                    valid = false;
                    break;
                }
            }

            if (valid){
                ans = get_mod(ans,solve(cols,i,n-1,dp));
            }
        }
        return dp[prev][n] = ans;
    }
public:
    int colorTheGrid(int m, int n) {
        string t = "";
        vector<string>cols;
        col_states(t,cols,m);
        vector<vector<int>>dp(cols.size()+1,vector<int>(n+1,-1));
        int cnt = 0;
        for (int i =0;i<cols.size();i++){
            cnt = get_mod(cnt,solve(cols,i,n-1,dp));
        }
        return cnt;
    }
};