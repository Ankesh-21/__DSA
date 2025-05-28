/*
* Leetcode : 3362
* T.C : O(N * QlogQ) // Q log Q for past and maxh
* S.C : O(Q)
*/
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        sort(queries.begin(), queries.end()); // sort by first element of each query

        priority_queue<int> maxh; // max-heap (stores negative of values to mimic Python's -heapq)
        priority_queue<int, vector<int>, greater<int>> past; // min-heap

        int usedQuery = 0;
        int j = 0;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            // Push new queries whose index matches current i
            while (j < queries.size() && queries[j][0] == i) {
                maxh.push(queries[j][1]); // pushing directly, no need to negate
                ++j;
            }

            nums[i] -= past.size();

            // While there are still max operations we can do and they are valid
            while (nums[i] > 0 && !maxh.empty() && maxh.top() >= i) {
                nums[i]--;
                int el = maxh.top(); maxh.pop();
                past.push(el);
                usedQuery++;
            }

            if (nums[i] > 0) return -1;

            // Remove past entries that expire at current i
            while (!past.empty() && past.top() == i) {
                past.pop();
            }
        }

        return queries.size() - usedQuery;
    }
};