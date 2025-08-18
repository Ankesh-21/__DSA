/*
* Leetcode : 679
* T.C : O(4 ^n + n ^ 2)
* S.C : O(1)
*/

class Solution {
    bool solve(vector<double>&c){
        if (c.size() == 1){
            return  abs(c[0]- 24.0) <= 1e-6; // if it lies in between 1e-6 range
        }
        
        for(int i = 0; i< c.size();i++){
            for (int j = 0; j < c.size();j++){
                if (i == j){
                    continue;
                }
                vector<double>temp;
                // Store that indices that we not proceed
                for(int k = 0; k < c.size();k ++){
                    if (i == k || j == k){ // if it is not proceed
                        continue;
                    }
                    temp.push_back(c[k]);
                }
                // For plus Operation
                temp.push_back(c[i] + c[j]);
                if (solve(temp))return true;
                temp.pop_back(); // Backtracking Step
                // For minus operation
                temp.push_back(c[i] - c[j]);
                if (solve(temp))return true;
                temp.pop_back();
                // For Multiplication Operation
                temp.push_back(c[i] * c[j]);
                if (solve(temp)) return true;
                temp.pop_back();
                // For Division Operation
                if (c[j] != 0)temp.push_back(c[i] / c[j]);
                if (solve(temp)) return true;
                temp.pop_back();
            }
        }
        return false;
    }
public:
    bool judgePoint24(vector<int>& cards) {
        // Converting the array double 
        vector<double>c;
        for(int i = 0; i<cards.size();i++){
            c.push_back(static_cast<double>(cards[i])); // using static_cast<double>(num)
        }
        return solve(c);
    }
};