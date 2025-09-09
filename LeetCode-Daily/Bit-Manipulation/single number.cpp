/*
@ leetcode : 136
@ T.C : O(N) // N is size of array
@ S.C : O(1)
*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xr = 0;
        for (int i = 0; i < nums.size();i++){
            xr = xr xor nums[i];
        }
        return xr;
    }
};