/*
* Leetcode : 2348
* T.C : O(N)
* S.C : O(1)
*/

class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        int i = 0;
        long long cnt = 0;
        int j ;
        for (j = 0; j < nums.size();j++){
            if (nums[j] == 0){
                continue;
            }
            if (i < j){
                while (i < j && nums[i] != 0){
                    i ++;
                }
                cnt += (long long)(j - i) * (long long)(j - i+1) / 2;
                i = j;
            }
        }
        if (i < j && j >= nums.size()){
            while (i < j && nums[i] != 0){
                i ++;
            }
            cnt += (long long)(j - i) * (long long)(j - i + 1) / 2;
        }
        return cnt;
    }
};