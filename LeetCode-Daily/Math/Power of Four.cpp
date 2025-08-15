/*
* Leetcode : 342
* T.C : O(1)
* S.C : O(1)
*/
class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0){
            return false;
        }
        int power = log10(n) / log10(4);
        return n == pow(4,power);
    }
};