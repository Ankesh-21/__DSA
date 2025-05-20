'''
* Leetcode : 3355
* T.C : O(N)
* S.C : O(N)
'''
# Topic Difference Array
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diffArray = [0 for _ in range(len(nums))]
        for query in queries:
            diffArray[query[0]] += 1
            if (query[1] + 1) < len(nums):
                diffArray[query[1]+1] -= 1
        for i in range(1,len(nums)):
            diffArray[i] += diffArray[i-1]
        # print(nums)
        # print(diffArray)
        for i in range(len(nums)):
            if nums[i] > diffArray[i]:
                return False
        return True