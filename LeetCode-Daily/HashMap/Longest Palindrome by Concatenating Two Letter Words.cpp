/*
* LeetCode: 2131
* T.C: O(N)
* S.C : O(N)
*/
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        // Result to store the length
        int result = 0;
        /*
        1. If reverseword in map use it else
        2. put into the map
        */
        unordered_map<string,int>mpp;
        for (auto&str:words){
            string revWord = str;
            swap(revWord[0],revWord[1]);
            if (mpp[revWord]>0){
                result += 4;
                mpp[revWord]--;
            }
            else{
                mpp[str] += 1;
            }
        }

        // Getting middle string which two chars will be same

        for (auto&el:mpp){
            string key = el.first;
            int freq = el.second;
            if (key[0]==key[1] && freq > 0){
                result += 2;
                break;
            }
        }

        return result;
    }
};