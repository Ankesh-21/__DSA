/*
@ leetcode : 137
@ T.C : O(31 * N) N is size of array
@ S.C : O(31)
*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int>setbits(32,0);
        // counting setbits of all numbers of that array
        // if no of setbits of that index like 2 
        // if setbits[2] % 3 == 1 then make that bit as set
        // beacause that signle number's bit will be set
        for(int i = 0; i < nums.size();i++){
            unsigned int num = nums[i]; // for -ve number
            for (int j = 0; j < 32;j++){
                // u for unsigned int
                // for -ve number
                if (((1u << j) & num) > 0){
                    setbits[j] += 1;
                }
            }
        }
        int num = 0;
        for (int i = 0; i < 32 ; i++){
            if ((setbits[i] % 3) == 1){
                num = (num | (1 << i));
            }
        }
        return num;
    }
};